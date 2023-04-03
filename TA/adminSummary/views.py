from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse

def admin_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    context = {'course_objects': course_objects}
    return render(response, "adminSummary.html", context)
