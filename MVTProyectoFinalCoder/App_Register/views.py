from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic   import ListView, DeleteView, CreateView, UpdateView, DetailView

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator
from django.contrib.auth.forms import UserChangeForm

from App_Register.forms import UserForm
from App_Register.models import Avatar
from .forms import AvatarForm, UserEditForm

# Create your views here.

def Register(request):

    if request.method == 'POST':

        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'El usuario: ' + username + ' fue creado con éxito!')

            return render(request, 'Register.html')

        else:
            for message in form.errors.values():
                messages.warning(request, message)

    else:

        form = UserForm()

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "Register.html", {"registerForm": form, "url":avatar.avatar.url})
    except:
        return render(request, "Register.html", {"registerForm": form})
    
@login_required
def UserEdit(request):
    usuario=request.user
    if(request.method=='POST'):
        userform=UserEditForm(request.POST, instance=request.user)
        if(userform.is_valid()):
            data=userform.cleaned_data
            usuario.first_name=data["first_name"]
            usuario.last_name=data["last_name"]
            usuario.email=data["email"]
            usuario.save()
            messages.success(request, "Datos actualizados con éxito!")
            return render(request,"UserEdit.html", {'userform':userform} )
    else:
        userform=UserEditForm(instance=request.user)

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "UserEdit.html", {"userform": userform, "url":avatar.avatar.url})
    except:
        return render(request, "UserEdit.html", {"userform": userform})

@login_required
def AddAvatar(request):
    if(request.method=='POST'):

        avatarform=AvatarForm(request.POST, request.FILES)

        if(avatarform.is_valid()):

            try:
                record = Avatar.objects.get(user_id = request.user.id)
                if record.id:
                    record.delete()
            except:
                print("Error, intente de nuevo...")

            data   = avatarform.cleaned_data
            avatar = Avatar(user=request.user, avatar = data["avatar"])
            avatar.save()
            messages.success(request, "Avatar agregado con éxito!")
            return redirect('AdminSite')
    else:
        avatarform=AvatarForm()

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "AddAvatar.html", {"avatarform": avatarform, "url":avatar.avatar.url})
    except:
        return render(request, "AddAvatar.html", {"avatarform": avatarform})

@method_decorator(login_required, name='dispatch')
class UserList(ListView):

    model               = User
    template_name       = './UserList.html'
    context_object_name = 'UserList'
