from django import forms 

from .models import CustomerFormModel

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerFormModel
        fields = [
            'firstName',
            'lastName',
            'email',
            'childFirstName',
            'childLastName',
            'anyAlergies'
        ]