from django.db import models
from django.db.models import Model

from multiselectfield import MultiSelectField

# Create your models here.
class CustomerFormModel(models.Model):
    allergens = (
        (1, 'milk'),
        (2, 'eggs'),
        (3, 'soybean'),
        (4, 'fish'),
        (5, 'shellfish'),
        (6, 'treenuts'),
        (7, 'peanuts'),
        (8, 'wheat')
    )

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    childFirstName = models.CharField(max_length=100)
    childLastName = models.CharField(max_length=100)
    anyAlergies = MultiSelectField(choices = allergens, max_choices = 8, max_length = 8)