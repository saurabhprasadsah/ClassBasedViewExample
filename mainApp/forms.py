from django import forms
from .models import Employee


class EmplyeeForm(forms.ModelForm):
    class Meta:
        model =Employee
        fields= ['name','email','phone','dsg','salary','city','state']