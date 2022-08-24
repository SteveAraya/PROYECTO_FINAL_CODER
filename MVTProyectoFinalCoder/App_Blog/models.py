from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Categoria(models.Model):
#     categoria = models.CharField(max_length=50)

#     class Meta:
#         verbose_name='categoria'
#         verbose_name_plural='categorias'

#     def __str__(self):
#         return self.nombre  

seleccion=[
    (1,'Estilo de vida'),
    (2,'Viajes'),
    (3,'Vehiculos')
]

class Categoria(models.Model):
    nombre = models.IntegerField(
            null=False, blank=False,
            choices=seleccion
            )

class Post(models.Model):
    categoria=models.ManyToManyField(Categoria)
    titulo = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=500)
    #autor = models.ManyToManyField(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    imagen = models.ImageField(upload_to='blog', blank=True, null=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo} - Subtitulo: {self.sub_titulo}'