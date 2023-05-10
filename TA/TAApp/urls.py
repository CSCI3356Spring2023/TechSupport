"""TAApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from application.views import application_view
from InstructorAddCourse.views import instructor_add_course_view
from adminSummary.views import admin_summary_view, send_email, edit_course, delete_course, show_applications
from instructorSummary.views import instructor_summary_view, instructor_show_applications
from studentSummary.views import student_summary_view, apply_course, edit_application, delete_application
from login.views import  login_home, logout, register, welcome


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', welcome, name= 'welcome'),
    path('login/', include("django.contrib.auth.urls")),
    path('login/', include('login.urls')),
    #path('logout/', logout, name = 'logout'),
    path('register/', register, name = 'register'),
    path('application/', application_view),
    path('add_course/', instructor_add_course_view, name = 'add_course'),
    path('admin_summary/', admin_summary_view),
    path('instructor_summary/', instructor_summary_view),
    path('student_summary/', student_summary_view),
    path('send_email/', send_email, name = 'send_email'),
    path("edit_course/<int:course_id>/", edit_course, name="edit_course"),
    path("apply_course/<int:course_id>/", apply_course, name="apply_course"),
    path("edit_application/<int:application_id>/", edit_application, name="edit_application"),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
    path('delete_application/<int:application_id>/', delete_application, name='delete_application'),
    path('show_applications/', show_applications, name='show_applications'),
     path('instructor_show_applications/', instructor_show_applications, name='instructor_show_applications'),

]


