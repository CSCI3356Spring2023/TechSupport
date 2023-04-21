from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse

# Create your views here.

def student_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    course_count = course_objects.count()
    context = {'course_objects': course_objects, 'course_count': course_count}
    return render(response, "studentSummary.html", context)
