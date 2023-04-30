from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomAuthenticationForm, RegistrationForm
from .models import CustomUser




@login_required
def login_home(request):
   if request.method == 'POST':
       form = CustomAuthenticationForm(request, data=request.POST)
       if form.is_valid():
           # Get the user's role from the logged-in user object
           role = request.user.role
          
           # Check if the user's role matches the selected role
           if role == 'S':
               return redirect('/student_summary')
           elif role == 'T':
               return redirect('/instructor_summary')
           elif role == 'A':
               return redirect('/admin_summary')
           else:
               messages.error(request, 'Invalid login credentials')
   else:
       form = CustomAuthenticationForm()
  
   return render(request, 'registration/login.html', {'form': form})


@login_required
def student_home(request):
   return render(request, 'student_home.html')


@login_required
def teacher_home(request):
   return render(request, 'teacher_home.html')


@login_required
def admin_home(request):
   return render(request, 'admin_home.html')




def register(request):
   if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           role = form.cleaned_data.get('role')
           major = form.cleaned_data.get('major')
           eagle_id = form.cleaned_data.get('eagle_id')
           year = form.cleaned_data.get('year')




           user = CustomUser.objects.create_user(
               username=username,
               password=password,
               role=role,  # Set the user's role based on the selected role
               major = major,
               eagle_id = eagle_id,
               year = year,
           )


           user.save()


           # Log the user in and redirect to the appropriate page based on their role
           login(request, user)
           if user.role == 'S':
               return redirect('/student_summary')
           elif user.role == 'T':
               return redirect('/instructor_summary')
           elif user.role == 'A':
               return redirect('/admin_summary')
   else:
       form = RegistrationForm()


   return render(request, 'register.html', {'form': form})




def logout_home(request):
   logout(request)
   return redirect('login_home')
