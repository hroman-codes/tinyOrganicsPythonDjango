from django import forms 

class Customer(forms.Form):
    firstName = forms.CharField(label='First name', max_length=100)