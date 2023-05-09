from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import InstructorAddCourseForm
from InstructorAddCourse.models import InstructorAddCourse



# Create your views here.

def instructor_add_course_view(request):
    if request.method == 'POST':
        form = InstructorAddCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.course_instructor = request.user
            course.save()
            return render(request, 'success.html')
        else:
            print(form.errors)
    else:
        form = InstructorAddCourseForm()
    return render(request, "addCoursePage.html", {'form': form})
