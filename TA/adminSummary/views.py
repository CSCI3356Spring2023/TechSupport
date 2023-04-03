from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse

def admin_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    course_count = course_objects.count()
    context = {'course_objects': course_objects, 'course_count': course_count}
    return render(response, "adminSummary.html", context)
