from django import forms

class ReservationForm(forms.Form):
    oficinaSalida  = forms.IntegerField()
    fechaSalida    = forms.DateField()
    horaSalida     = forms.TimeField()  
    oficinaLlegada = forms.IntegerField()
    fechaLlegada   = forms.DateField()
    horaLlegada    = forms.TimeField() 
    vehiculo       = forms.IntegerField()
    nombreConductor         = forms.CharField() 
    identificacionConductor = forms.CharField() 
    telefonoConductor       = forms.CharField() 
    edadConductor           = forms.IntegerField() 
    correoConductor         = forms.CharField() 
