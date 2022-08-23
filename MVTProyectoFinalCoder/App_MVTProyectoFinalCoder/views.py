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

# class ContactUsList(ListView):

#     model               = Contact
#     template_name       = './ContactUsList.html'
#     context_object_name = 'ContactList'

#------------------- CAR VIEWS -------------------#
# class CarList(ListView):

#     model               = Car
#     template_name       = './Car/CarList.html'
#     context_object_name = 'CarList'

# class CarCreate(CreateView):
#     model         = Car
#     template_name = './Car/CarCreate.html'
#     form_class: CarForm
#     fields        = [ 
#         "tipo", 
#         "marca", 
#         "modelo", 
#         "placa", 
#         "annio", 
#         "tipo_caja",
#         "combustible", 
#         "cantidad_pasajeros",
#         "numero_puertas"
#     ]
#     success_url   = '/carList/' 

# def CarSearch(request):

#     return render(request, './Car/CarSearch.html')

# def Search(request):
 

#     if request.GET["carName"]:

#         carToSearch = request.GET["carName"]

#         carList = Car.objects.filter(marca__icontains=carToSearch)

#         return render(request, "ResultSearch.html", {"carList": carList, "marca": carToSearch})

#     else:

#         respuesta = "No enviaste datos"

#     return HttpResponse(respuesta)

# class CarUpdate(UpdateView):

#     model = Car
#     template_name = './Car/car_update.html'
#     fields = ('__all__')
#     success_url = '/carList/'

# class CarDelete(DeleteView):

#     model = Car
#     template_name = './Car/car_delete.html'
#     success_url = '/carList/'

#------------------- OFFICE VIEWS -------------------#
# class OfficeList(ListView):

#     model               = Office
#     template_name       = './Office/OfficeList.html'
#     context_object_name = 'OfficeList'

# class OfficeCreate(CreateView):
#     model         = Office
#     template_name = './Office/OfficeCreate.html'
#     form_class: OfficeForm
#     fields        = [ 
#         "nombre", 
#         "ubicacion", 
#         "telefono", 
#         "horario"
#     ]
#     success_url   = '/OfficeList/' 


# class OfficeUpdate(UpdateView):

#     model = Office
#     template_name = './Office/Office_update.html'
#     fields = ('__all__')
#     success_url = '/OfficeList/'

# class OfficeDelete(DeleteView):

#     model = Office
#     template_name = './Office/Office_delete.html'
#     success_url = '/OfficeList/'