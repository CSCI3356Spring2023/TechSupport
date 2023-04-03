from django.urls import path
from .views import  login_home, student_home, teacher_home, admin_home, logout, register

urlpatterns = [
    path('', login_home, name='login_home'),
    path('student/', student_home, name='student_home'),
    path('teacher/', teacher_home, name='teacher_home'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout/', logout, name = 'logout'),
    path('register/', register, name = 'register'),
]
