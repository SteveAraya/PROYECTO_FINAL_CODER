from django.urls import path
from django.contrib.auth import views as auth_views

from App_MVTProyectoFinalCoder.views import (
    Home, 
    AdminSite,
    AboutUs,
    Logout,
)

urlpatterns = [    

    path('', Home,  name='Home'),
    path('adminSite', AdminSite,  name='AdminSite'),
    path('aboutUs', AboutUs,  name='AboutUs'),
    path("logout", Logout, name= "Logout"),

]