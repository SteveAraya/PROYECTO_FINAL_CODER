from django.http          import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.shortcuts     import  render, redirect
from django.contrib.auth  import logout
from django.contrib       import messages

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

def AdminSite(self):
    return render(self, "Admin.html")

def Logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/login')

def PageNotFound(request, exception):
    return render(request, "PageNotFound.html")
