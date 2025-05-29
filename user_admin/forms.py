from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

ACCOUNT_TYPE_CHOICES = [
    ('viewer', 'Viewer'),
    ('editor', 'Editor'),
    # Do NOT include 'admin' unless you want anyone to register as admin!
]


class EmployeeIDAuthenticationForm(forms.Form):
    employee_id = forms.CharField(label="Employee ID")
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    second_name = forms.CharField(required=True)
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html(),)
    password2 = forms.CharField(widget=forms.PasswordInput)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, label="Account Type")
    class Meta:
        model = UserProfile
        fields = [
            'first_name', 'second_name', 'employee_id', 
            'contact_no','employee_email', 'position', 'department'
        ]

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        user = User(username=self.cleaned_data.get('employee_id'))
        try:
            validate_password(password, user)
        except ValidationError as e:
            self.add_error('password1', e)
        return password

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            self.add_error('password2', "Passwords do not match.")
        return cleaned_data