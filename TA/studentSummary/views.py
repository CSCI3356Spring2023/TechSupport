from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from django.shortcuts import render, redirect, get_object_or_404
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application 
from login.models import CustomUser
from application.forms import ApplicationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST


# Create your views here.

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

    pending_applications = Application.objects.filter(student=response.user, is_approved=False)
    approved_applications = Application.objects.filter(student=response.user, is_approved=True)
    rejected_applications = Application.objects.filter(student=response.user, is_rejected=True)

    print(f'User: {response.user}')
    print(f'Application Objects: {application_objects}')

    context = {'course_objects': course_objects,
               'course_count': course_count,
               'pending_applications': pending_applications,
               'approved_applications': approved_applications,
               'rejected_applications': rejected_applications,
               'term_keys': term_keys,
               'dept_keys': dept_keys,
               'curr_user': curr_user}

    return render(response, "studentSummary.html", context)


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

        return redirect(request.session.get('previous_url', '/'))
    else:
        request.session['previous_url'] = request.META.get('HTTP_REFERER', '/')
        form = ApplicationForm(request.POST)
        context = {'application': application,
               'form': form}
        return render(request, "edit_application.html", context)


def delete_application(request, application_id):
    course = get_object_or_404(Application, id=application_id)
    course.delete()
    return redirect(student_summary_view)

@login_required
@require_POST
def accept_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    course = InstructorAddCourse.objects.get(course_number=application.course_number)
    # increment the curr_num_ta field
    course.curr_num_ta += 1
    course.save()
    application.student_response = 'A'
    application.save()

    # Prevent student from accepting or applying for more positions
    other_applications = Application.objects.filter(student=request.user).exclude(id=application_id)
    for app in other_applications:
        app.is_approved = False
        app.save()

    return redirect(student_summary_view)

@login_required
@require_POST
def decline_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    application.student_response = 'D'
    application.save()

    return redirect(student_summary_view)
