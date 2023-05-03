from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application

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

term_keys = InstructorAddCourse.objects.values_list(
    'term', flat=True).distinct()
dept_keys = sorted(list(set([get_dept(course)
                   for course in InstructorAddCourse.objects.all()])))
status_keys = ['Open', 'Closed']

def instructor_summary_view(response):
    # database objects
    course_objects = InstructorAddCourse.objects.all()
    course_count = course_objects.count()
    applications = Application.objects.all()

    # search terms
    search_query = response.GET.get('q', '')
    term_filter = response.GET.get('term', '')
    status_filter = response.GET.get('status', '')
    dept_filter = response.GET.get('dept-code', '')
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

    
    context = {'course_objects': course_objects,
               'course_count': course_count,
               'application_objects': applications,
               'applied_filters': applied_filters,
               'term_keys': term_keys,
               'dept_keys': dept_keys}
    return render(response, "instructorSummary.html", context)