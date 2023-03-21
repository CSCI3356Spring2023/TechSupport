from django.http import HttpResponse
from django.shortcuts import render
from .forms import InstructorAddCourse
# Create your views here.

def instructor_add_course_view(request, *args, **kwargs):#args, and key word args
	if request.method == 'POST':
		form = InstructorAddCourse(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'success.html')
	else:
		form = InstructorAddCourse()
	return render(request, "addCoursePage.html", {'form': form})
