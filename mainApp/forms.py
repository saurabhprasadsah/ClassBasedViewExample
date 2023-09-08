from django import forms
from .models import Employee


class EmplyeeForm(forms.Form):
    class Meta:
        