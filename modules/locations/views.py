from django.shortcuts import render
from django.views.generic import TemplateView

def home_page(request):
    return render(request, 'locations/home.html')
