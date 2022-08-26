from django.shortcuts       import render

from django.views.generic   import ListView, DeleteView, CreateView, UpdateView, DetailView

from App_Office.models      import Office
from App_Car.models         import Car
from App_Reservation.models import Reservation
from App_Reservation.forms  import ReservationForm

from django.contrib         import messages

# Create your views here.

def CreateReservation(request):

    cars     = Car.objects.all()
    offices  = Office.objects.all()
    contexto = {"cars": cars, "offices": offices}

    if(request.method=="POST"):

        reservationForm = ReservationForm(request.POST)

        if(reservationForm.is_valid()):
            data = reservationForm.cleaned_data
            reservation = Reservation(
                oficinaSalida  = data["oficinaSalida"],
                fechaSalida    = data["fechaSalida"],
                horaSalida     = data["horaSalida"],
                oficinaLlegada = data["oficinaLlegada"],
                fechaLlegada   = data["fechaLlegada"],
                horaLlegada    = data["horaLlegada"],
                vehiculo       = data["vehiculo"],
                nombreConductor         = data["nombreConductor"],
                identificacionConductor = data["identificacionConductor"],
                telefonoConductor       = data["telefonoConductor"],
                edadConductor           = data["edadConductor"],
                correoConductor         = data["correoConductor"],
            )

            print("Entre al form..............")
            print("Entre al form..............")
            print("Entre al form..............")
            print("Entre al form..............")

            # reservation.oficinaSalida  = Self.request.oficinaSalida
            # reservation.oficinaLlegada = Self.request.oficinaLlegada
            # reservation.vehiculo       = Self.request.vehiculo

            reservation.save()
            messages.success(request, 'La reserva se realizo con éxito!')
            return render(request, "Reservation.html", contexto)

        else:
            for message in reservationForm.errors.values():
                messages.warning(request, message)

    else:
        return render(request, "Reservation.html", contexto)
