from django.shortcuts       import render

from django.views.generic   import ListView, DeleteView, CreateView, UpdateView, DetailView

from App_Office.models      import Office
from App_Car.models         import Car
from App_Reservation.models import Reservation
from App_Reservation.forms  import ReservationForm

from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

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
                oficinaSalida  = Office(request.POST["oficinaSalida"]),
                fechaSalida    = data["fechaSalida"],
                horaSalida     = data["horaSalida"],
                oficinaLlegada = Office(request.POST["oficinaLlegada"]),
                fechaLlegada   = data["fechaLlegada"],
                horaLlegada    = data["horaLlegada"],
                vehiculo       = Car(request.POST["vehiculo"]),
                nombreConductor         = data["nombreConductor"],
                identificacionConductor = data["identificacionConductor"],
                telefonoConductor       = data["telefonoConductor"],
                edadConductor           = data["edadConductor"],
                correoConductor         = data["correoConductor"],
            )

            reservation.save()
            messages.success(request, 'La reserva se realizo con éxito!')
            return render(request, "Reservation.html", contexto)

        else:
            for message in reservationForm.errors.values():
                messages.warning(request, message)

    else:
        return render(request, "Reservation.html", contexto)

@method_decorator(login_required, name='dispatch')
class ReservationList(ListView):

    model               = Reservation
    template_name       = './ReservationList.html'
    context_object_name = 'ReservationList'