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
            'state':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter state Name'}),
            
        } 
    def clean(self):
        cleaned_data= super().clean()
        name= self.cleaned_data['name']
        email= self.cleaned_data['email']
        phone= self.cleaned_data['phone']
        dsg= self.cleaned_data['dsg']

        
        if(len(name)<3):
            raise forms.ValidationError("name at least contain 3 charater!")
        if(len(email)<13):
            raise forms.ValidationError("email id not valid!")
        if(len(phone)<3):
            raise forms.ValidationError("phone at least contain 10 number!")
        if(len(dsg)<3):
            raise forms.ValidationError("dsg at least contain 3 charater!")



        


        

