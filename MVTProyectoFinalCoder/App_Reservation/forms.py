from django import forms

class ReservationForm(forms.Form):
    fechaSalida    = forms.DateField()
    horaSalida     = forms.TimeField()
    fechaLlegada   = forms.DateField()
    horaLlegada    = forms.TimeField() 
    nombreConductor         = forms.CharField() 
    identificacionConductor = forms.CharField() 
    telefonoConductor       = forms.CharField() 
    edadConductor           = forms.IntegerField() 
    correoConductor         = forms.CharField() 
