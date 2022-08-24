from django import forms

class OfficeForm(forms.Form):
    nombre    = forms.CharField()
    ubicacion = forms.CharField()
    telefono  = forms.CharField()  
    horario   = forms.CharField()