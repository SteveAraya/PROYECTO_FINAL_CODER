from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    categoria = models.CharField(max_length=50, null=True)
    titulo = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=5000)
    #autor = models.ManyToManyField(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    imagen = models.ImageField(upload_to='blog', blank=True, null=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo} - Subtitulo: {self.sub_titulo}'