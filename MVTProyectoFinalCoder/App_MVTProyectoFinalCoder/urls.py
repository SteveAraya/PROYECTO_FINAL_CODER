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
    # path('logout', auth_views.LogoutView.as_view(), name='Logout'),


    # path('createCar/', CarCreate.as_view(), name="CarCreate"),
    # path('carList/', CarList.as_view(), name="CarList"),

    # path('officeCreate/', OfficeCreate.as_view(), name="OfficeCreate"),
    # path('officeList/', OfficeList.as_view(), name="OfficeList"),

]