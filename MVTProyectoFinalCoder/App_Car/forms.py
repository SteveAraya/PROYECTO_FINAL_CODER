from dataclasses import fields
from tkinter import Widget
from django import forms

from .models import Car

# categoria = [
#     ('Coche','Coche'),
#     ('Vehiculo de carga','Vehiculo de carga'),
#     ('Vehiculo utilitario','Vehiculo utilitario'),
#     ('Vehiculo deportivo','Vehiculo deportivo'),
# ]

class CarForm(forms.Form):
    categoria          = forms.CharField()
    tipo               = forms.CharField()
    marca              = forms.CharField()
    modelo             = forms.CharField()
    placa              = forms.CharField()
    annio              = forms.IntegerField()
    tipo_caja          = forms.CharField()
    combustible        = forms.CharField()
    cantidad_pasajeros = forms.IntegerField()
    numero_puertas     = forms.IntegerField()
    imagen             = forms.ImageField()
    control_crucero    = forms.BooleanField(required=False)
    radio              = forms.BooleanField(required=False)
    aacond             = forms.BooleanField(required=False)
    bluetooth          = forms.BooleanField(required=False)
    cierrepuertas      = forms.BooleanField(required=False)

    # class Meta:
    #     model=Car
    #     fields=('__all__')
    #     widgets={
    #         'categoria':forms.ChoiceField(
    #             attrs={
    #                 'class':'form-select'
    #             }
    #         )
    #     }


    # class Meta:
    #     fields = ('categoria','tipo', 'marca', 'modelo', 'placa' ,'annio' )

    # def __init__(self, *args, **kwargs): 
    #     super().__init__(*args, **kwargs) 
    #     self.fields['modelo'].widget.attrs.update({ 
    #         'class':'form-control', 
    #         'required':'true', 
    #         'name':'modelo', 
    #         'id':'modelo', 
    #         'type':'text', 
    #         'placeholder':'Ingrese el modelo del vehículo...', 
    #         'maxlength': '20', 
    #         'minlength': '3', 
    #     })
    #     self.fields['categoria'].widget.attrs.update({ 
    #         'class':'form-select', 

    #     }) 