from django.urls import path

from App_Reservation.views import (
    Reservation,
)

urlpatterns = [    

    path('', Reservation,  name='Reservation'),

]