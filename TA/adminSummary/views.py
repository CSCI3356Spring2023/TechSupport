from django.shortcuts import render, redirect
from django.core.mail import send_mail
from InstructorAddCourse.models import InstructorAddCourse

term_keys = ['Spring 2023', 'Fall 2024', 'Spring 2024']
dept_keys = ['CSCI', 'ECON', 'PHIL']
status_keys = ['Open', 'Closed']


def admin_summary_view(response):
    search_query = response.GET.get('q', '')
    term_filter = response.GET.get('term', '')
    status_filter = response.GET.get('status', '')
    dept_filter = response.GET.get('dept-code', '')

    course_objects = InstructorAddCourse.objects.all()
    applied_filters = []
    if search_query:
        course_objects = course_objects.filter(
            course_name__icontains=search_query)
        applied_filters.append(('q', search_query))

    if term_filter:
        if term_filter in term_keys:
            course_objects = [course for course in course_objects if get_term(
                course) == term_filter]
            applied_filters.append(('term', term_filter))

    if dept_filter:
        if dept_filter in dept_keys:
            course_objects = [course for course in course_objects if get_dept(
                course) == dept_filter]
            applied_filters.append(('dept-code', dept_filter))

    if status_filter:
        if status_filter in status_keys:
            course_objects = [course for course in course_objects if get_status(
                course) == status_filter]
            applied_filters.append(('status', status_filter))
    else:
        applied_filters = [f for f in applied_filters if f[0] != 'status']

    course_count = len(course_objects)
    context = {'course_objects': course_objects,
               'course_count': course_count, 'applied_filters': applied_filters}

    return render(response, "adminSummary.html", context)


def get_term(course):
    return course.term


def get_dept(course):
    dept_code = ""
    for i in course.course_number:
        if i.isalpha():
            dept_code = "".join([dept_code, i])
    return dept_code


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
