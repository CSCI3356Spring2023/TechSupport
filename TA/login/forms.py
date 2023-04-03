from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

# Define choices for the role field
ROLE_CHOICES = [    ('S', 'Student'),    ('T', 'Teacher'),    ('A', 'Admin'),]

from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    role = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        #self.fields['role'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Role'})

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        if not role:
            raise forms.ValidationError('Role is required.')
        return cleaned_data


# Create a custom registration form that includes the role field
class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']
