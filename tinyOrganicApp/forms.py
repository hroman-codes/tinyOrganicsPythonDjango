from django import forms 

from .models import CustomerFormModel

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerFormModel
        fields = [
            'First_Name',
            'Last_Name',
            'Email',
            'Child_First_Name',
            'Child_Last_Name',
            'Any_Allergies'
        ]