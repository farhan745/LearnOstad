from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
  #?part1:
  '''title=forms.CharField(
    label='task',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Task'}),
  )'''
  class Meta:
    
    model = Task
    fields = [
      'title',
      'completed',
    ]
    #?part 2:
    def __init__(self):
      super().__init__(*args, **kwargs)
      self.fields['title'].label = "Task Title"
      self.fields['title'].widgets.attrs.update({'class': 'form-control'})
      self.fields['completed'].label = "Task Completed"
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'x' in title:
          raise forms.ValidationError('Task name cannot contain the letter x')
        
        return title
    