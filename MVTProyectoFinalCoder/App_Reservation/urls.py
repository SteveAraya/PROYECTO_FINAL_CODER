from django.urls import path

from App_Reservation.views import (
    CreateReservation,
    ReservationList,
)

urlpatterns = [    

    path('', CreateReservation,  name='Reservation'),
    path('reservationList/', ReservationList.as_view(), name="ReservationList"),

]