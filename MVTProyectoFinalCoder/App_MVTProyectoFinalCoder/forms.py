from django import forms

class CarForm(forms.Form):
    tipo               = forms.CharField()
    marca              = forms.CharField()
    modelo             = forms.CharField()  
    placa              = forms.CharField()
    annio              = forms.IntegerField()
    tipo_caja          = forms.CharField()
    combustible        = forms.CharField()
    cantidad_pasajeros = forms.IntegerField()
    numero_puertas     = forms.IntegerField()

class OfficeForm(forms.Form):
    nombre    = forms.CharField()
    ubicacion = forms.CharField()
    telefono  = forms.CharField()  
    horario   = forms.CharField()

class ContactUsForm(forms.Form):
    asunto             = forms.CharField()
    comentario         = forms.CharField()
    nombre_completo    = forms.CharField()  
    correo_electronico = forms.CharField()