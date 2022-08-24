from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from django.contrib import messages


from App_Register.forms import UserForm

# Create your views here.

def Register(request):

    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'El usuario: ' + username + ' fue creado con éxito!')

            return redirect('/createUser')

        else:
            for message in form.errors.values():
                messages.warning(request, message)

    else:

        form = UserForm()

    return render(request, "Register.html", {"registerForm": form})
    