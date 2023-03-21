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
            # Get the user's role from the logged-in user object
            role = request.user.role
            
            # Check if the user's role matches the selected role
            if role == 'S':
                return redirect('/student')
            elif role == 'T':
                return redirect('/teacher')
            elif role == 'A':
                return redirect('/admin_home')
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


def logout(request):
    return redirect('login')