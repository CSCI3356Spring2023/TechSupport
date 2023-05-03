from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InstructorAddCourseForm
from InstructorAddCourse.models import InstructorAddCourse



# Create your views here.

def instructor_add_course_view(request):
    if request.method == 'POST':
        form = InstructorAddCourseForm(request.POST)
        print("AYOOOOO")
        if form.is_valid():
            print("FORM IS VALID")
            form.save()
            return render(request, 'success.html')
        else:
            print(form.errors)
    else:
        form = InstructorAddCourseForm()
    return render(request, "addCoursePage.html", {'form': form})
