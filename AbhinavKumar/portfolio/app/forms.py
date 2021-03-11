from django.core import validators
from django import forms
from .models import Data

class Employee(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','email','phone','Project']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'Project': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the Project name...'})
        }