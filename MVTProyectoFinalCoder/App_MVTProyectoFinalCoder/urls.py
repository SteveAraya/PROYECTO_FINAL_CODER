from django.urls import path

from App_MVTProyectoFinalCoder.views import (
    Home, 
    ContactUS,
    ContactUsList,
    CarCreate, 
    CarList,
    CarSearch,
    Search,
    # CarUpdate,
    # CarDelete,
    OfficeCreate,
    OfficeList,
    # OfficeUpdate,
    # OfficeDelete,
)

urlpatterns = [    

    path('', Home,  name='Home'),

    path('contact/', ContactUS, name="Contact"),
    path('contactList/', ContactUsList.as_view(), name="ContactUsList"),

    path('createCar/', CarCreate.as_view(), name="CarCreate"),
    path('carList/', CarList.as_view(), name="CarList"),
    path('carSearch/', CarSearch, name="CarSearch"),
    path('search/', Search, name="Search"),
    # path('carUpdate/', CarUpdate.as_view(), name="CarUpdate"),
    # path('carDelete/', CarDelete.as_view(), name="CarDelete"),

    path('officeCreate/', OfficeCreate.as_view(), name="OfficeCreate"),
    path('officeList/', OfficeList.as_view(), name="OfficeList"),
    # path('officeUpdate/', OfficeUpdate.as_view(), name="OfficeUpdate"),
    # path('officeDelete/', OfficeDelete.as_view(), name="OfficeDelete"),

]