from django.urls import path
from . import views
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('filteredRecipes/', views.filteredRecipesTest, name='filteredRecipes'),
    path('form/filteredRecipes.html', views.filteredRecipesTest, name='filteredRecipes'),
    path('sentry-debug/', trigger_error),
]