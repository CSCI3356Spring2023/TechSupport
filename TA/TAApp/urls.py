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
from adminSummary.views import admin_summary_view, send_email
from instructorSummary.views import instructor_summary_view
from studentSummary.views import student_summary_view


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('', include('login.urls')),
    path('application/', application_view),
    path('add_course/', instructor_add_course_view),
    path('admin_summary/', admin_summary_view),
    path('instructor_summary/', instructor_summary_view),
    path('student_summary/', student_summary_view),
<<<<<<< Updated upstream
    path('send_email/', send_email, name = 'send_email')
=======
    path('', include("django.contrib.auth.urls")),
>>>>>>> Stashed changes
]


