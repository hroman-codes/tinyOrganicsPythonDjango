from django.db import models
from django.db.models import Model

# Create your models here.
class CustomerForm(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    childFirstName = models.CharField(max_length=100)
    childLastName = models.CharField(max_length=100)
    anyAlergies = models.CharField(max_length=100)
