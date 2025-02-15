from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = [
      'title',
      'completed',
    ]
    def clean_titles(self):
      title = self.cleaned_data.get('title')
      if "x" in title:
        raise forms.ValidationError('Title can not contain x')
      return title