from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse

# Create your views here.

def student_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    context = {'course_objects': course_objects}
    return render(response, 'studentSummary.html', context)
