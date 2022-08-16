from django.db import models

# Create your models here.

class Car(models.Model):
    tipo               = models.CharField(max_length=50)
    marca              = models.CharField(max_length=50)
    modelo             = models.CharField(max_length=50)
    placa              = models.CharField(max_length=50)
    annio              = models.IntegerField()
    tipo_caja          = models.CharField(max_length=50)
    combustible        = models.CharField(max_length=50)
    cantidad_pasajeros = models.IntegerField()
    numero_puertas     = models.IntegerField()