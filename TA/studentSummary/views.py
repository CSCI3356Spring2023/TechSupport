from django.shortcuts import render
from InstructorAddCourse.models import InstructorAddCourse
from django.shortcuts import render, redirect, get_object_or_404
from InstructorAddCourse.models import InstructorAddCourse
from application.models import Application 
from login.models import CustomUser


# Create your views here.

def student_summary_view(response):
    course_objects = InstructorAddCourse.objects.all()
    course_count = course_objects.count()
    application_objects = application.objects.all
    context = {'course_objects': course_objects, 'course_count': course_count, 'application_objects': application_objects}
    return render(response, "studentSummary.html", context)


def edit_application(request, application_id):
    application = get_object_or_404(InstructorAddCourse, id=application_id)
    if request.method == "POST":

        application.course_number = request.POST['course_number']
        application.first_name = request.POST['first_name']
        application.last_name = request.POST['last_name']
        application.eagle_id = request.POST['eagle_id']
        application.grad = request.POST['grad']
        application.past_course = request.POST['past_course']
        application.grade = request.POST['grade']
        application.hours = request.POST['hours']
        application.other_courses = request.POST['other_courses']
        application.misc_information = request.POST['misc_information']
        
        # course.course_name = request.POST['course_name']
        # course.course_number = request.POST['course_number']
        # course.course_instructor = request.POST['course_instructor']
        # course.course_description = request.POST['course_description']
        # course.total_time_commitment = request.POST['total_time_commitment']
        # course.has_discussion = request.POST['has_discussion']
        # course.num_ta_needed = request.POST['num_ta_needed']
        # course.curr_num_ta = request.POST['curr_num_ta']
        # course.graded_meeting = request.POST['graded_meeting']
        # course.office_hours = request.POST['office_hours']
        # course.other_info = request.POST['other_info']
        # course.term = request.POST['term']
        
        application.save()
        return redirect(student_summary_view)
    else:
        return render(request, "application.html", {"course": course})


def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(id=request.user.id)
            if user.can_apply():
                user.increment_applications()
                user.save()
                form.save()
                return render(request, 'success.html')
            else:
                form.add_error(None, "You have already applied to 5 courses (maximum number of applications)")
        else:
            form = ApplicationForm()
        return render(request, 'application.html', {'form': form})
    else:
        form = ApplicationForm()
    return render(request, 'application.html', {'form': form})
