from django import forms

import task.forms
from task.models import Task

from .models import Developer


class DeveloperForm(forms.ModelForm):
    # first_name = forms.CharField(label="First name", max_length=100)
    # last_name = forms.CharField(max_length=100)
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name']


class TaskForm(task.forms.TaskForm):
    def clean_status(self):
        # when field is cleaned, we always return the existing model field.
        return self.instance.status

    def __init__(self, *args, **kwargs):
        super(task.forms.TaskForm, self).__init__(*args, **kwargs)
