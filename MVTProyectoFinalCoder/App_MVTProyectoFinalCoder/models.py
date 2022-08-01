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

class Office(models.Model):
    nombre    = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=500)
    telefono  = models.CharField(max_length=50)
    horario   = models.CharField(max_length=200)

class Contact(models.Model):
    asunto             = models.CharField(max_length=100)
    comentario         = models.CharField(max_length=500)
    nombre_completo    = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100)