from django.http          import HttpResponse
from django.shortcuts     import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView


from App_MVTProyectoFinalCoder.models import Contact, Car, Office
from App_MVTProyectoFinalCoder.forms  import CarForm, OfficeForm, ContactUsForm


# Create your views here.

def Home(self):
    return render(self, "Home.html")

#------------------- ContactUS VIEWS -------------------#
def ContactUS(self):
    
    if (self.method == 'POST'):

        contactForm = ContactUsForm(self.POST)

        if contactForm.is_valid():
            data    = contactForm.cleaned_data
            contact = Contact(
                asunto=data['asunto'], 
                comentario=data['comentario'], 
                nombre_completo=data['nombre_completo'], 
                correo_electronico=data['correo_electronico']
            )
            print(contact)
            contact.save()
            return render(self,'Home.html')

    else:
        return render(self, "ContactUs.html")

class ContactUsList(ListView):

    model               = Contact
    template_name       = './ContactUsList.html'
    context_object_name = 'ContactList'

#------------------- CAR VIEWS -------------------#
class CarList(ListView):

    model               = Car
    template_name       = './Car/CarList.html'
    context_object_name = 'CarList'

class CarCreate(CreateView):
    model         = Car
    template_name = './Car/CarCreate.html'
    form_class: CarForm
    fields        = [ 
        "tipo", 
        "marca", 
        "modelo", 
        "placa", 
        "annio", 
        "tipo_caja",
        "combustible", 
        "cantidad_pasajeros",
        "numero_puertas"
    ]
    success_url   = '/carList/' 


class CarUpdate(UpdateView):

    model = Car
    template_name = './Car/car_update.html'
    fields = ('__all__')
    success_url = '/carList/'

class CarDelete(DeleteView):

    model = Car
    template_name = './Car/car_delete.html'
    success_url = '/carList/'

#------------------- OFFICE VIEWS -------------------#
class OfficeList(ListView):

    model               = Office
    template_name       = './Office/OfficeList.html'
    context_object_name = 'OfficeList'

class OfficeCreate(CreateView):
    model         = Office
    template_name = './Office/OfficeCreate.html'
    form_class: OfficeForm
    fields        = [ 
        "nombre", 
        "ubicacion", 
        "telefono", 
        "horario"
    ]
    success_url   = '/OfficeList/' 


class OfficeUpdate(UpdateView):

    model = Office
    template_name = './Office/Office_update.html'
    fields = ('__all__')
    success_url = '/OfficeList/'

class OfficeDelete(DeleteView):

    model = Office
    template_name = './Office/Office_delete.html'
    success_url = '/OfficeList/'