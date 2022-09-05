from django.shortcuts     import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms               import OfficeForm
from .models              import Office

from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

#------------------- OFFICE VIEWS -------------------#
@method_decorator(login_required, name='dispatch')
class OfficeList(ListView):
    model               = Office
    template_name       = './OfficeList.html'
    context_object_name = 'OfficeList'

class OfficeListHome(ListView):
    model               = Office
    template_name       = './OfficeListHome.html'
    context_object_name = 'OfficeListHome'

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class OfficeDelete(DeleteView):

    model         = Office
    template_name = 'OfficeDelete.html'
    success_url   = '/office/officeList/'