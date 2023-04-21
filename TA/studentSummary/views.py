from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from django.shortcuts import render, redirect, get_object_or_404
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application 
from login.models import CustomUser
from application.forms import ApplicationForm


# Create your views here.

def student_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    course_count = course_objects.count()
    application_objects = Application.objects.all
    context = {'course_objects': course_objects, 'course_count': course_count, 'application_objects': application_objects}
    return render(response, "studentSummary.html", context)


def apply_course(request, course_id):
    course = get_object_or_404(InstructorAddCourse, id=course_id)
    # application = Application.objects.filter(course=course, user=request.user).first()

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.course = course
            application.save()
            return redirect(student_summary_view)
    else:
        form = ApplicationForm(initial={'course': course})
        
    return render(request, 'application.html', {'form': form, 'course': course})

def edit_application(request, application_id):
   
    application = get_object_or_404(Application, id=application_id)
    if request.method == "POST":

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




