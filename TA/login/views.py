from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def login_home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get the user's role from the form data
            role = request.POST.get('role')
            
            # Authenticate the user's credentials
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            
            # Check if the user's role matches the selected role
            if user is not None and user.groups.filter(name=role).exists():
                login(request, user)
                if role == 'student':
                    return render('/student')
                elif role == 'teacher':
                    return render('/teacher')
                elif role == 'admin':
                    return render('/admin')
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def student_home(request):
    return render(request, 'student_home.html')

@login_required
def teacher_home(request):
    return render(request, 'teacher_home.html')

@login_required
def admin_home(request):
    return render(request, 'admin_home.html')
