from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('filteredRecipes/', views.filteredRecipesTest, name='filteredRecipes'),
    path('form/filteredRecipes.html', views.filteredRecipesTest, name='filteredRecipes')
]