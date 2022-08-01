from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(self):
    return render(self, "home.html")

def contact(self):
    return HttpResponse(f'Estas viendo la vista de Contacto')

def car(self):
    return HttpResponse(f'Estas viendo la vista de Vehiculos')

def office(self):
    return HttpResponse(f'Estas viendo la vista de Oficinas')