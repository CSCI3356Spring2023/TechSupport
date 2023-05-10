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
   ('2026', '2026'),
   ('2025', '2025'),
   ('2024', '2024'),
   ('2023', '2023'),
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
   first_name = forms.CharField(max_length = 20, required = True)
   last_name = forms.CharField(max_length = 20, required = True)

   major = forms.ChoiceField(choices=MAJOR_CHOICES, required=False)
   eagle_id = forms.CharField(max_length=8, required=False)
   year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)


   def clean(self):
       cleaned_data = super().clean()
       role = cleaned_data.get('role')
       first_name = cleaned_data.get('first_name')
       last_name = cleaned_data.get('last_name')
       major = cleaned_data.get('major')
       eagle_id = cleaned_data.get('eagle_id')
       year = cleaned_data.get('year')


       if role == 'S':
           if (major == 'NA' or not eagle_id or year == 'NA'):
               raise forms.ValidationError("Please fill out all required fields for student registration")
           
       if (not first_name or not last_name):
           raise forms.ValidationError("Please fill out the fields First Name and Last Name")


       return cleaned_data


   class Meta(UserCreationForm.Meta):
       model = CustomUser
       fields = ['username', 'password1', 'password2', 'role', 'first_name', 'last_name', 'major', 'eagle_id', 'year']
