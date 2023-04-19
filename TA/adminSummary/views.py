from django.shortcuts import render, redirect
from django.core.mail import send_mail 
from InstructorAddCourse.models import InstructorAddCourse

def admin_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    query = response.GET.get('q')
    if query:
        course_objects = course_objects.filter(course_name__icontains=query)
    if response.GET.get('my_checkbox'):
        course_objects = course_objects.filter(has_discussion=True)
    course_count = course_objects.count()
    context = {'course_objects': course_objects, 'course_count': course_count}

    

    return render(response, "adminSummary.html", context)

def send_email(response):
        send_mail(
            'Example Subject',
            'Example message.',
            'swe2023testing@gmail.com',
            ['yangbam@bc.edu'],
            fail_silently=False,
        )
        return redirect(admin_summary_view)