from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application

# Create your views here.
def instructor_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    application_objects = Application.objects.all()
    context = {'course_objects': course_objects,
               'application_objects': application_objects}
    return render(response, "instructorSummary.html", context)