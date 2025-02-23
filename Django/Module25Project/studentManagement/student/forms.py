from django import forms
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        exclude = ['user']
       # fields = '__all__'
        labels = {
            "name": " Name",
            "photo": "Upload Photo",
        }
        help_text = {"email": "Email will be Confidential"}
    password = forms.CharField(widget=forms.PasswordInput())


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']