from django import forms
from .models import Developer


class DeveloperForm(forms.ModelForm):
    # first_name = forms.CharField(label="First name", max_length=100)
    # last_name = forms.CharField(max_length=100)
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name']
