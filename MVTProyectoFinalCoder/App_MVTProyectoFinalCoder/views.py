from django.http          import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.shortcuts     import  render, redirect
from django.contrib.auth  import logout
from django.contrib       import messages

#from App_Register.models import Avatar
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

from App_Register.models import Avatar

# Create your views here.

def Home(self):
    return render(self, "Home.html")

def AboutUs(request):
    history_steve  = False
    history_adrian = False
    if request.GET.get('view_history_steve'):
        history_steve = True
        context = {'history_steve': history_steve, 'history_adrian': history_adrian}
    elif request.GET.get('close_history_steve'):
        history_steve = False
        context = {'history_steve': history_steve, 'history_adrian': history_adrian}
    elif request.GET.get('view_history_adrian'):
        history_adrian = True
        context = {'history_adrian': history_adrian, 'history_steve': history_steve,}
    elif request.GET.get('close_history_adrian'):
        history_adrian = False
        context = {'history_adrian': history_adrian, 'history_steve': history_steve,}
    else:
        context = {'history_steve': history_steve, 'history_adrian': history_adrian}

    return render(request, "AboutUs.html", context)

    
@login_required
def AdminSite(request):
    try:
        avatar=Avatar.objects.get(user=request.user.id)
        return render(request, "Admin.html", {"url":avatar.avatar.url})
    except:
        return render(request, "Admin.html")

 
def Logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/login')

def PageNotFound(request, exception):
    return render(request, "PageNotFound.html")

