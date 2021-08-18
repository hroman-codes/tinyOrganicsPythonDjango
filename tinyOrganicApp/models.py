from django.db import models
from django.db.models import Model

from multiselectfield import MultiSelectField
import requests

# Create your models here.
def fetchAllergens(requests):
        response = requests.get('https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/')
        allergens = response.json()
        listOfAllergens = []

        for allergen in allergens:
            listOfAllergens.append((allergen['name'], allergen['name']))
        
        return listOfAllergens

class CustomerFormModel(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Child_First_Name = models.CharField(max_length=100)
    Child_Last_Name = models.CharField(max_length=100)
    Any_Allergies = MultiSelectField(choices = fetchAllergens(requests))