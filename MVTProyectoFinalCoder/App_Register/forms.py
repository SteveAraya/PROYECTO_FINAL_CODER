from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from App_Register.models import Avatar
 

class UserForm(UserCreationForm):

    first_name = forms.CharField(max_length=20, label=False) 
    last_name  = forms.CharField(max_length=30, label=False) 
    username   = forms.CharField(max_length=20, label=False) 
    email      = forms.EmailField(max_length=100)

    class Meta:
        model  = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2')

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['first_name'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'first_name', 
            'id':'first_name', 
            'type':'text', 
            'placeholder':'Nombre', 
            'maxlength': '20', 
            'minlength': '3', 
        }) 

        self.fields['last_name'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'last_name', 
            'id':'last_name', 
            'type':'text', 
            'placeholder':'Apellidos', 
            'maxlength': '30', 
            'minlength': '3', 
        }) 

        self.fields['username'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Usuario', 
            'maxlength': '20', 
            'minlength': '6', 
        }) 

        self.fields['email'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'example@gmail.com', 
        }) 

        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'Contraseña', 
            'maxlength':'22',  
            'minlength':'8' 
        }) 

        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'Confirmar Contraseña', 
            'maxlength':'22',  
            'minlength':'8' 
        }) 

class UserEditForm(UserChangeForm):
    password=forms.Field(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    class Meta:
        model=User
        fields=['email','first_name','last_name']

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['first_name'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'first_name', 
            'id':'first_name', 
            'type':'text', 
            'placeholder':'Nombre', 
            'maxlength': '20', 
            'minlength': '3', 
        }) 

        self.fields['last_name'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'last_name', 
            'id':'last_name', 
            'type':'text', 
            'placeholder':'Apellidos', 
            'maxlength': '30', 
            'minlength': '3', 
        }) 

        self.fields['email'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'example@gmail.com', 
        }) 

class AvatarForm(forms.ModelForm):
    class Meta:
        model=Avatar
        fields=("avatar",)
