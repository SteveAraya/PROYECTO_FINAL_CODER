
from django import forms
from django.contrib.auth.models import User
from .models import Categoria

class CatForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['nombre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class':'control-form'
        })

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