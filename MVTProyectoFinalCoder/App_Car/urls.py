from django.urls import path

from App_Car.views import (
    CarCreate,
)

urlpatterns = [    

    path('create', CarCreate,  name='CarCreate'),

]