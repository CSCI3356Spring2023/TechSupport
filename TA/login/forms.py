from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser


# Define choices for the role field
ROLE_CHOICES = [   
   ('S', 'Student'),   
   ('T', 'Teacher'),   
   ('A', 'Admin'),
]


# Define choices for the major field
MAJOR_CHOICES = [
   ('NA', 'NA'),
   ('BA', 'Bachelor of Arts in Computer Science'),
   ('BS', 'Bachelor of Science in Computer Science'),
   ('Minor', 'Computer Science Minor'),
]


# Define choices for the cohort field
YEAR_CHOICES = [
   ('NA', 'NA'),
   ('Freshman', 'Freshman'),
   ('Sophomore', 'Sophomore'),
   ('Junior', 'Junior'),
   ('Senior', 'Senior'),
]


class CustomAuthenticationForm(AuthenticationForm):
   role = forms.CharField()


   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
       self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
       


   def clean(self):
       cleaned_data = super().clean()
       role = cleaned_data.get('role')
       if not role:
           raise forms.ValidationError('Role is required.')
       return cleaned_data




# Create a custom registration form that includes the role field
class RegistrationForm(UserCreationForm):
   role = forms.ChoiceField(choices=ROLE_CHOICES)


   major = forms.ChoiceField(choices=MAJOR_CHOICES, required=False)
   eagle_id = forms.CharField(max_length=8, required=False)
   year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)


   def clean(self):
       cleaned_data = super().clean()
       role = cleaned_data.get('role')
       major = cleaned_data.get('major')
       eagle_id = cleaned_data.get('eagle_id')
       year = cleaned_data.get('year')


       if role == 'S':
           if (major == 'NA' or not eagle_id or year == 'NA'):
               raise forms.ValidationError("Please fill out all required fields for student registration")


       return cleaned_data


   class Meta(UserCreationForm.Meta):
       model = CustomUser
       fields = ['username', 'password1', 'password2', 'role', 'major', 'eagle_id', 'year']
