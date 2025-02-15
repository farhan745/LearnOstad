from django import forms
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"
        labels = {
            "name": "Student Name",
            "photo": "Upload Photo",
        }
        help_text = {"email": "Email will be Confidential"}
    password = forms.CharField(widget=forms.PasswordInput())
