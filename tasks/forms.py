from django import forms
from tasks.models import *

class TaskForm(forms.ModelForm):
  class Meta:
    model = TaskModel
    fields = '__all__'
  
  widgets = {
    'due_date': forms.DateInput(attrs={'type': 'date'})
  }


