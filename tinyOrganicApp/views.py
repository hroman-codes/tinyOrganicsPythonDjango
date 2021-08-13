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
    # return HttpResponseRedirect('/filteredRecipes')

def filteredRecipesTest(request):
    obj = CustomerFormModel.objects.get(id=1)
    print(obj)

    # context = {
    #     'First_Name': obj.First_Name,
    #     'Last_Name': obj.Last_Name,
    #     'Email': obj.Email,
    #     'Child_First_Name': obj.Child_First_Name,
    #     'Child_Last_Name': obj.Child_Last_Name,
    #     'Any_Allergies': obj.Any_Allergies,
    # }

    context = {
        'object': obj
    }

    return render(request, 'tinyOrganicApp/filteredRecipes.html', context)