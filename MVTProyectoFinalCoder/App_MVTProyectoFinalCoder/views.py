from django.http          import HttpResponse
from django.shortcuts     import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

# Create your views here.

def Home(self):
    return render(self, "Home.html")

def AdminSite(self):
    return render(self, "Admin.html")

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