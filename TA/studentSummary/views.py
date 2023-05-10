from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from django.shortcuts import render, redirect, get_object_or_404
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application 
from login.models import CustomUser
from application.forms import ApplicationForm
from django.contrib.auth.decorators import login_required

term_keys = ['Spring 2023', 'Summer 2023', 'Fall 2024', 'Spring 2024']
dept_keys = ['CSCI', 'ECON', 'PHIL', 'ARTH', 'HIST', 'ENGL', 'MATH', 'POLI']
status_keys = ['Open', 'Closed']

# Create your views here.


@login_required
def student_summary_view(response):
    search_query = response.GET.get('q', '')
    term_filter = response.GET.get('term', '')
    status_filter = response.GET.get('status', '')
    dept_filter = response.GET.get('dept-code', '')
    applied_filters = []

    course_objects = InstructorAddCourse.objects.all()

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
    application_objects = Application.objects.filter(student=response.user)
    curr_user = response.user
    print(f'User: {response.user}')
    print(f'Application Objects: {application_objects}')

    context = {'course_objects': course_objects, 'course_count': course_count, 'application_objects': application_objects, 'curr_user': curr_user}
    return render(response, "studentSummary.html", context)

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

def apply_course(request, course_id):

    course = get_object_or_404(InstructorAddCourse, id=course_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST) 
        
        #Form is never valid, trying to fix
        if form.is_valid():
            user = CustomUser.objects.get(id=request.user.id)
            if user.can_apply():
                user.increment_applications()
                user.save()
                
                application = form.save(commit=False)
                application.student = request.user
                print(f'Before Saving: {application}')
                application.save()
                print(f'Saved Application: {application}')
                return render(request, 'success.html')
        else: 
            print(form.errors)
            return render(request, 'application.html', {'form': form, 'course': course})

    else:
      
    # Only create the application object after checking form validity
        form = ApplicationForm()
        return render(request, 'application.html', {'form': form, 'course': course})



def edit_application(request, application_id):
   
    application = get_object_or_404(Application, id=application_id)
    if request.method == "POST":

        application.course_name = request.POST['course_name']
        application.course_number = request.POST['course_number']
        application.description = request.POST['description']
        application.first_name = request.POST['first_name']
        application.last_name = request.POST['last_name']
        application.eagle_id = request.POST['eagle_id']
        application.grad = request.POST['grad']
        application.past_course = request.POST['past_course']
        application.grade = request.POST['grade']
        application.hours = request.POST['hours']
        application.other_courses = request.POST['other_courses']
        application.misc_information = request.POST['misc_information']
        
        application.save()

        return redirect(student_summary_view)
    else:

        form = ApplicationForm(request.POST)
        context = {'application': application,
               'form': form}
        return render(request, "edit_application.html", context)



def delete_application(request, application_id):
    course = get_object_or_404(Application, id=application_id)
    course.delete()
    return redirect(student_summary_view)
