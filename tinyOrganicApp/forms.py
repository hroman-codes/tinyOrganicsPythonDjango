from django import forms 

from .models import CustomerModelForm

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModelForm
        fields = [
            'firstName',
            'lastName',
            'email',
            'childFirstName',
            'childLastName',
            'anyAlergies'
        ]