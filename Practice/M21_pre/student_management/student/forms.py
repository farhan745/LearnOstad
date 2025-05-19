from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = models.Student
        exclude = ['user']
        labels = {
            'name': "Full Name",
            'email': "Email Address",
            'phone': "Phone Number",
            'password': "Password",
            'photo': "Profile Picture"
        }
        
        help_text ={
            'name': "Please enter your full name",
            'email': "Please enter a valid email address",
            'phone': "Please enter a valid phone number",
            'password': "Please enter a strong password",
            'photo': "Please upload a profile picture"
        }
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']