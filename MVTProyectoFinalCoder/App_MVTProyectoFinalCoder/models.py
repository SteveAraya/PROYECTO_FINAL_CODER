from email.message import EmailMessage
from itertools import pairwise
from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    Nombre
    Apellido
    Email
    Pais

class Curso(models.Model):
    Nombre
    Descripcion
    FechaInicio
    FechaFin

class Profesor(models.Model):
    Nombre
    Apellido
    Email
    Pais
    Profesion
