from django.shortcuts import render, redirect
from InstructorAddCourse.models import InstructorAddCourse
from django.contrib.auth.models import User
from application.models import Application
from django.contrib.auth.decorators import login_required

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


@login_required
def instructor_summary_view(response):
    search_query = response.GET.get('q', '')
    term_filter = response.GET.get('term', '')
    status_filter = response.GET.get('status', '')
    dept_filter = response.GET.get('dept-code', '')

    current_user = response.user
    course_objects = InstructorAddCourse.objects.filter(course_instructor=current_user)

    term_keys = course_objects.values_list('term', flat=True).distinct()
    dept_keys = sorted(list(set([get_dept(course)
                   for course in course_objects])))
    status_keys = sorted(list(set([get_status(course)
                   for course in course_objects])))


    applied_filters = []
    if search_query:
        course_objects = course_objects.filter(
            course_name__icontains=search_query)
        applied_filters.append(('q', search_query))

    if term_filter and term_filter in term_keys:
        course_objects = course_objects.filter(term=term_filter)
        applied_filters.append(('term', term_filter))

    if dept_filter and dept_filter in dept_keys:
        course_objects = course_objects.filter(course_number__istartswith=dept_filter)
        applied_filters.append(('dept-code', dept_filter))

    if status_filter and status_filter in status_keys:
        course_objects = [course for course in course_objects if get_status(course) == status_filter]
        applied_filters.append(('status', status_filter))

    else:
        applied_filters = [f for f in applied_filters if f[0] != 'status']

    applications = []
    if 'course_number' in response.session:
        course_number = response.session['course_number']
        applications = Application.objects.filter(course_number=course_number)
        del response.session['course_number']

    course_count = len(course_objects)
    context = {'course_objects': course_objects,
               'course_count': course_count, 'applied_filters': applied_filters,
               'term_keys': term_keys, 'dept_keys': dept_keys,
               'applications': applications}

    return render(response, "instructorSummary.html", context)

def instructor_show_applications(request):
    if request.method == "POST":
        course_number = request.POST['course_number']
        request.session['course_number'] = course_number
        return redirect(instructor_summary_view)
    else:
        return redirect(instructor_summary_view)
