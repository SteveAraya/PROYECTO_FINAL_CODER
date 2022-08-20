from django import forms

class ContactUsForm(forms.Form):
    asunto             = forms.CharField()
    comentario         = forms.CharField()
    nombre_completo    = forms.CharField()  
    correo_electronico = forms.CharField()