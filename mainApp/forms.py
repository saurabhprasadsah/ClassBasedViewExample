from django import forms
from .models import Employee

class EmplyeeForm(forms.ModelForm):
    class Meta: #meta will be represent the innner class Employeeform
        model =Employee
        fields= ['name','email','phone','dsg','salary','city','state']
        widgets= {
            'name':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter name'}),
            'email':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter email id'}),
            'phone':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter phone Number'}),
            'dsg':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter Designation'}),
            'salary':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter salary'}),
            'city':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter city Name'}),
            'state':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter state Name'})
        } 