from django.urls import path

from App_Reservation.views import (
    CreateReservation,
)

urlpatterns = [    

    path('', CreateReservation,  name='Reservation'),

]