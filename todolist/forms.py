from django import forms
from .models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


def __init__(self):
    self.priority = 3
