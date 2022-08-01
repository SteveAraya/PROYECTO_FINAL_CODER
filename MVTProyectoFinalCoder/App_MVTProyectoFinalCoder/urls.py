from django.urls import path
from App_MVTProyectoFinalCoder.views import home, contact, car, office
from . import views

urlpatterns = [    
    path('', home),
    path('contact/', contact),
    path('car/', car),
    path('office/', office),
]