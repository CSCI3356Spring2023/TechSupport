from django import forms
from .models import InstructorAddCourse

class InstructorAddCourseForm(forms.ModelForm):
    class Meta:
        model = InstructorAddCourse
        fields = ('course_name', 'course_number', 'course_instructor', 'course_description', 'total_time_commitment', 'has_discussion','num_ta_needed', 'office_hours', 'graded_meeting','other_info')
        widgets = {

            'couse_name': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'couse_number': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'couse_instructor': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'couse_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'total_time_commitment': forms.NumberInput(attrs={'class': 'form-control', 'rows': 3}),
            'has_discussion': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'num_ta_needed': forms.NumberInput(attrs={'class': 'form-control', 'rows': 3}),
            'office_hours': forms.NumberInput(attrs={'class': 'form-control', 'rows': 3}),
            'graded_meeting': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

        }
    
    def __init__(self, *args, **kwargs):
        super(InstructorAddCourseForm, self).__init__(*args, **kwargs)
    
        
        self.fields['course_name'].label = 'Course Name'

        self.fields['course_number'].label = 'Course Number'

        self.fields['course_instructor'].label = 'Course Instructor'

        self.fields['course_description'].label = 'Course Description'
        
        self.fields['total_time_commitment'].label = 'Total Time Commitment'

        self.fields['has_discussion'].label = 'Has a Discussion?'

        self.fields['num_ta_needed'].label = 'Number of TAs Needed?'

        self.fields['office_hours'].label = 'Number of Office Hours per Week'

        self.fields['graded_meeting'].label = 'Assignments Graded in Meeting?'

        self.fields['other_info'].required = False
