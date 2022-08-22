from django.db import models

# Create your models here.

class Car(models.Model):
    categoria          = models.CharField(max_length=50, null=True)
    tipo               = models.CharField(max_length=50)
    marca              = models.CharField(max_length=50)
    modelo             = models.CharField(max_length=50)
    placa              = models.CharField(max_length=50)
    annio              = models.IntegerField()
    tipo_caja          = models.CharField(max_length=50)
    combustible        = models.CharField(max_length=50)
    cantidad_pasajeros = models.IntegerField()
    numero_puertas     = models.IntegerField()
    imagen             = models.ImageField(upload_to='car', blank=True, null=True)
    control_crucero    = models.BooleanField(null=True, blank=False)
    radio              = models.BooleanField(null=True, blank=False)
    aacond             = models.BooleanField(null=True, blank=False)
    bluetooth          = models.BooleanField(null=True, blank=False)
    cierrepuertas      = models.BooleanField(null=True, blank=False)

    def __str__(self):
        return f'Categoria: {self.categoria} Tipo: {self.tipo} - Marca: {self.marca} - Modelo: {self.modelo} - Placa: {self.placa}'