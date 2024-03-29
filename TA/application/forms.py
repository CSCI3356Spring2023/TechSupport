from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):


    class Meta:
        model = Application
        fields = ('course_name','course_number', 'description','first_name', 'last_name', 'eagle_id', 'grad','past_course', 'grade', 'hours', 'other_courses', 'misc_information')
        widgets = {

            
            'past_course': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'grade': forms.Select(attrs={'class': 'form-select'}),
            'grad': forms.Select(attrs={'class': 'form-select'}),
            'hours': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'other_courses': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'misc_information': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.fields['course_name'].label = "Course Name"
        self.fields['course_number'].label = "Course Number"
        self.fields['description'].label = "Description"
        self.fields['other_courses'].required = False
        self.fields['misc_information'].required = False
        self.fields['past_course'].label = 'Have you taken this course in the past?'
        self.fields['grade'].label = 'If so, what grade did you receive'
        self.fields['hours'].label = 'How many hours can you commit to the position?'
        self.fields['other_courses'].label = 'What other relevant courses have you taken?'
        self.fields['misc_information'].label = 'Answers to extra questions, misc. information'
        self.fields['first_name'].label = 'First name'
        self.fields['last_name'].label = 'Last name'
        self.fields['eagle_id'].label = 'Eagle ID'
        self.fields['grad'].label = 'Graduation year'
        # self.fields['course_name'].required = False
        # self.fields['course_number'].required = False
        # self.fields['description'].required = False


