from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import CustomerFormModel
import requests
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'tinyOrganicApp/base.html')

def form(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()
        return redirect('filteredRecipes.html')

    context = {
        'form': form,
    }

    return render(request, 'tinyOrganicApp/form.html', context)

def filteredRecipesTest(request):
    # get the last entry in the DB 
    # specifically the allergens 
    obj = CustomerFormModel.objects.last()
    print('obj.Any_Allergies >>>', obj.Any_Allergies)
    
    # fetch the recipes API once the LOADS || on init
    response = requests.get('https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/')
    recipes = response.json()

    badRecipes = []
    recipeNames = []
    
    # loop through the recipes against the allergens
        # - target the allergen property save that in a var for clarity 
        # - if the allergens array contains 
    for recipe in recipes:
        recipeNames.append(recipe['name'])

        for allergen in recipe['allergens']:
            print('allergen >>>', allergen)
            if obj.Any_Allergies.count(allergen) > 0:
                badRecipes.append(recipe['name'])

    # helper filter function to sniff out the good recipes 
    def filterRecipe(rec):
        return False if rec in badRecipes else True

    # save the filtered recipes in a variable 
    filteredRecipes = filter(filterRecipe, recipeNames)
    listFilteredRecipes = tuple(filteredRecipes)

    print('badRecipes >>', badRecipes)
    print('filteredRecipes', list(filteredRecipes))
    # print('listFilteredRecipes', listFilteredRecipes)
                
    # send it to the context object 
    # >> use the template to loop through it and spit out all the filtered recipes
    context = {
        'object': obj,
        'listFilteredRecipes': listFilteredRecipes,
        'badRecipes': badRecipes
    }

    return render(request, 'tinyOrganicApp/filteredRecipes.html', context)