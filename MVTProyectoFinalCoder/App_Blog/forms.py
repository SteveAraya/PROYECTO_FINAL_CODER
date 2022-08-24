
from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    categoria = forms.CharField()
    titulo = forms.CharField()
    sub_titulo = forms.CharField()
    cuerpo = forms.CharField()
    # autor = forms.ModelMultipleChoiceField(
    #         queryset=User.objects.all()
    #         widgets=forms.checkb
    # )
    fecha = forms.DateField()
    imagen = forms.ImageField()