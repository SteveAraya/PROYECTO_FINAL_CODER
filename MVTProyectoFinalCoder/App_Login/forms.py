from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Usuario...', 
            'maxlength': '20', 
            'minlength': '6', 
        }) 

        self.fields['password'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'name':'password', 
            'id':'password', 
            'type':'password', 
            'placeholder':'Contraseña...', 
            'maxlength':'22',  
            'minlength':'8' 
        }) 
