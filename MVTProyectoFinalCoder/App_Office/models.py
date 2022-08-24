from django.db import models

# Create your models here.

class Office(models.Model):
    nombre    = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=500)
    telefono  = models.CharField(max_length=50)
    horario   = models.CharField(max_length=200)