from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomAuthenticationForm, RegistrationForm
from .models import CustomUser





def login_home(request):
   
   if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.role == 'S':
                login(request, user)
                return redirect('/student_summary')
            elif user.role == 'T':
                login(request, user)
                return redirect('/instructor_summary')
            elif user.role == 'A':
                login(request, user)
                return redirect('/admin_summary')
            else:
                messages.success(request, ("Users must have a role to continue..."))
                return redirect('login')
            
        else:
            messages.success(request, ("Username or Password is incorrect, Try Again..."))	
            return redirect('login')
        	
   else:
       return render(request, 'authenticate/login.html', {})

def welcome(request):
    return render(request, 'welcome.html')


def register(request):
   if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           role = form.cleaned_data.get('role')
           first_name = form.cleaned_data.get('first_name')
           last_name = form.cleaned_data.get('last_name')
           major = form.cleaned_data.get('major')
           eagle_id = form.cleaned_data.get('eagle_id')
           year = form.cleaned_data.get('year')
           email = form.cleaned_data.get('email')




           user = CustomUser.objects.create_user(
               username=username,
               password=password,
               role=role,  # Set the user's role based on the selected role
               major = major,
               eagle_id = eagle_id,
               first_name = first_name,
               last_name = last_name,
               year = year,
               email = email,
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
