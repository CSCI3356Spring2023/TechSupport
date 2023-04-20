from django.shortcuts import render, redirect
from django.core.mail import send_mail
from InstructorAddCourse.models import InstructorAddCourse


def admin_summary_view(response):
    search_query = response.GET.get('q', '')
    status_filter = response.GET.get('status', '')

    course_objects = InstructorAddCourse.objects.all()
    applied_filters = []
    if search_query:
        course_objects = course_objects.filter(
            course_name__icontains=search_query)
        applied_filters.append(('q', search_query))

    if status_filter:
        if status_filter in ['Open', 'Closed']:
            course_objects = [course for course in course_objects if get_status(
                course) == status_filter]
            applied_filters.append(('status', status_filter))
    else:
        applied_filters = [f for f in applied_filters if f[0] != 'status']

    if response.GET.get('my_checkbox'):
        course_objects = course_objects.filter(has_discussion=True)
    course_count = len(course_objects)
    context = {'course_objects': course_objects,
               'course_count': course_count, 'applied_filters': applied_filters}

    return render(response, "adminSummary.html", context)


def get_status(course):
    return "Open" if course.curr_num_ta < course.num_ta_needed else "Closed"


def send_email(response):
    send_mail(
        'Example Subject',
        'Example message.',
        'swe2023testing@gmail.com',
        ['yangbam@bc.edu'],
        fail_silently=False,
    )
    return redirect(admin_summary_view)
