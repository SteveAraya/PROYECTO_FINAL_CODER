from django.db import models

from App_Car.models import Car
from App_Office.models import Office

# Create your models here.

class Reservation(models.Model):
    oficinaSalida   = models.ForeignKey(Office, related_name='oficinaSalida', on_delete=models.CASCADE)
    fechaSalida     = models.DateField()
    horaSalida      = models.TimeField()
    oficinaLlegada  = models.ForeignKey(Office, related_name='oficinaLlegada', on_delete=models.CASCADE)
    fechaLlegada    = models.DateField()
    horaLlegada     = models.TimeField()
    vehiculo        = models.ForeignKey(Car, on_delete=models.CASCADE)
    nombreConductor         = models.CharField(max_length=200)
    identificacionConductor = models.CharField(max_length=200)
    telefonoConductor       = models.CharField(max_length=50)
    edadConductor           = models.IntegerField()
    correoConductor         = models.CharField(max_length=200)