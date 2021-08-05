from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import CustomerFormModel
import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello tinyOrganic Hire me for this job")

def form(request):
    # response = requests.get('https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/')
    # data = response.json()
    # print(data)
    # return render(request, 'tinyOrganicApp/test.html', {'response': response})
    
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()

    context = {
        'form': form
    }

    return render(request, 'tinyOrganicApp/form.html', context)