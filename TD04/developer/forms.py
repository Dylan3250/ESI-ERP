from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
import task.forms
from .models import Developer


class DeveloperForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email')


class DeveloperChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email')


class TaskForm(task.forms.TaskForm):
    def clean_status(self):
        # when field is cleaned, we always return the existing model field.
        return self.instance.status

    def __init__(self, *args, **kwargs):
        super(task.forms.TaskForm, self).__init__(*args, **kwargs)


class ShortDeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'username']
