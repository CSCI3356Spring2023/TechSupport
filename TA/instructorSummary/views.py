from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application

# Create your views here.
def instructor_summary_view(response):
    # database objects
    course_objects = InstructorAddCourse.objects.all()
    application_objects = Application.objects.all()

    # search terms
    search_query = response.GET.get('q', '')

    applied_filters = []

    if search_query:
        course_objects = course_objects.filter(
            course_name__icontains=search_query)
        applied_filters.append(('q', search_query))

    context = {'course_objects': course_objects,
               'application_objects': application_objects}
    return render(response, "instructorSummary.html", context)