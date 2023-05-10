from django import template
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application

register = template.Library()

@register.filter
def has_existing_application(course, user):
    applications = Application.objects.filter(student=user)
    courses = InstructorAddCourse.objects.all()
    for application in applications:
        for course_obj in courses:
            if application.course_number == course_obj.course_number:
                if course == course_obj:
                    return True
    return False