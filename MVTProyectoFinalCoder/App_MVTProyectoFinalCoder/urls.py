from django.urls import path
from App_MVTProyectoFinalCoder.views import home

urlpatterns = [    
    path('', home),
]