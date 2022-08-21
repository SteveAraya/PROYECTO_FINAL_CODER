from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib import messages

from App_Login.forms import LoginForm


def Login(request):

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario = data["username"]
            psw     = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return redirect('/contact-us/contactList')

            else:

                return redirect('/login')

        messages.error(request, 'Usuario/Contraseña incorrecta.')

    else:

        form = LoginForm()

    return render(request, "Login.html", {"loginForm": form})
