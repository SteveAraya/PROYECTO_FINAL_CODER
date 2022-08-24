from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import OfficeForm
from .models import Office

# Create your views here.

#------------------- OFFICE VIEWS -------------------#
class OfficeList(ListView):
    model               = Office
    template_name       = './OfficeList.html'
    context_object_name = 'OfficeList'

class OfficeCreate(CreateView):
    model         = Office
    template_name = './OfficeCreate.html'
    form_class: OfficeForm
    fields        = [ 
        "nombre", 
        "ubicacion", 
        "telefono", 
        "horario"
    ]
    success_url   = '/office/officeList/' 

# class OfficeUpdate(UpdateView):

#     model = Office
#     template_name = './Office/Office_update.html'
#     fields = ('__all__')
#     success_url = '/OfficeList/'

class OfficeDelete(DeleteView):

    model         = Office
    template_name = 'OfficeDelete.html'
    success_url   = '/office/officeList/'