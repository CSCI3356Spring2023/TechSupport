from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application

# Create your views here.
def instructor_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    course_count = course_objects.count()
    application_objects = Application.objects.all()
    context = {'course_objects': course_objects, 'course_count': course_count,
               'application_objects': application_objects}
    return render(response, "instructorSummary.html", context)