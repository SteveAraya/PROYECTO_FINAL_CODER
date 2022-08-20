from django.db import models

# Create your models here.

class Contact(models.Model):
    asunto             = models.CharField(max_length=100)
    comentario         = models.CharField(max_length=500)
    nombre_completo    = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100)