from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello tinyOrganic I want this job.")

def form(request):
    response = requests.get('https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/')
    data = response.json()
    print(data)
    return render(request, 'tinyOrganicApp/test.html', {'response': response})