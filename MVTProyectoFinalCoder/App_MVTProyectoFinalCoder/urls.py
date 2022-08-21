from django.urls import path

from App_MVTProyectoFinalCoder.views import (
    Home, 
    AdminSite,
)

urlpatterns = [    

    path('', Home,  name='Home'),
    path('adminSite', AdminSite,  name='AdminSite'),

    # path('createCar/', CarCreate.as_view(), name="CarCreate"),
    # path('carList/', CarList.as_view(), name="CarList"),

    # path('officeCreate/', OfficeCreate.as_view(), name="OfficeCreate"),
    # path('officeList/', OfficeList.as_view(), name="OfficeList"),

]