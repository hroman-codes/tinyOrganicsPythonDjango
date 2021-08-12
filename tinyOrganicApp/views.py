from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import CustomerFormModel
import requests

# Create your views here.
def index(request):
    return render(request, 'tinyOrganicApp/base.html')

def form(request):
     
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()

    context = {
        'form': form,
    }

    return render(request, 'tinyOrganicApp/form.html', context)