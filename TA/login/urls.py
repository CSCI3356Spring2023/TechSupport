from django.urls import path
from .views import  login_home, student_home, teacher_home, admin_home, logout

urlpatterns = [
    path('', login_home, name='login'),
    path('student/', student_home, name='student_home'),
    path('teacher/', teacher_home, name='teacher_home'),
    path('admin/', admin_home, name='admin_home'),
    path('logout/', logout, name = 'logout')
]
