from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Define choices for the role field
ROLE_CHOICES = [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('admin', 'Admin'),
]

# Create a custom login form that includes the role field
class CustomAuthenticationForm(AuthenticationForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    # Override the default clean method to validate the role field
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        role = self.cleaned_data.get('role')

        # Use Django's built-in authentication backend to validate the user's credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # Check if the user belongs to the selected role
            if role == 'student' and user.is_student:
                return self.cleaned_data
            elif role == 'teacher' and user.is_teacher:
                return self.cleaned_data
            elif role == 'admin' and user.is_admin:
                return self.cleaned_data

        # If the user's credentials or role are invalid, raise a validation error
        raise forms.ValidationError('Invalid login credentials')

