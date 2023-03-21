from django import forms
from .models import InstructorAddCourse

class InstructorAddCourseForm(forms.ModelForm):
    class Meta:
        model = InstructorAddCourse
        fields = ('course_name', 'course_number', 'course_instructor', 'course_description', 'has_discussion', 'graded_meeting', 'num_hours', 'other_info')
        widgets = {
            'course_name': forms.RadioSelect(attrs={'class': 'horizontal-list', 'id':'past'}),
            'num_hours': forms.NumberInput(attrs={'min': 0}),
            'other_info': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super(InstructorAddCourse, self).__init__(*args, **kwargs)
        #self.fields['other_courses'].required = False
        
        self.fields['course_name'].label = 'Course Name'

        self.fields['course_number'].label = 'Course Number'

        self.fields['course_instructor'].label = 'Course Instructor'

        self.fields['course_description'].label = 'Course Description'

        self.fields['has_discussion'].label = 'Has a Discussion?'

        self.fields['graded_meeting'].label = 'Assignments Graded in Meeting?'

        self.fields['num_hours'].label = 'Number of Hours per Week'

        self.fields['other_info'].required = False
