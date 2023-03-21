from django.http import HttpResponse
from django.shortcuts import render
from .forms import InstructorAddCourseForm


# Create your views here.

def instructor_add_course_view(request):
    if request.method == 'POST':
        form = InstructorAddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = InstructorAddCourseForm()
    return render(request, "addCoursePage.html", {'form': form})

