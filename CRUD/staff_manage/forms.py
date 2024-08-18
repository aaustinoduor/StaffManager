from django import forms
from staff_manage.models import Staff

class StaffInfoForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields="__all__"
        labels={
            'fname':'First Name',
            'lname':'Last Name',
            'email':'Email',
            'phone':'Phone No',
                        
        }
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'course':forms.Select(attrs={'class': 'form-control'}),
        }