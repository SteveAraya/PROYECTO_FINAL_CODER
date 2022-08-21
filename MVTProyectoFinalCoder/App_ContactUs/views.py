from django.http          import HttpResponse
from django.shortcuts     import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from App_ContactUs.models import Contact
from App_ContactUs.forms  import ContactUsForm

from django.contrib import messages

# Create your views here.

#------------------- ContactUS VIEWS -------------------#
def ContactUS(request):
    
    if (request.method == 'POST'):

        contactForm = ContactUsForm(request.POST)

        if contactForm.is_valid():
            data    = contactForm.cleaned_data
            contact = Contact(
                asunto=data['asunto'], 
                comentario=data['comentario'], 
                nombre_completo=data['nombre_completo'], 
                correo_electronico=data['correo_electronico']
            )
            contact.save()
            messages.success(request, 'El mensaje fue enviado con éxito!')
            return render(request,'ContactUS.html')

        else:
            for message in contactForm.errors.values():
                messages.warning(request, message)

    else:
        return render(request, "ContactUS.html")

class ContactUsList(ListView):

    model               = Contact
    template_name       = './ContactUsList.html'
    context_object_name = 'ContactList'

class ContactUsDelete(DeleteView):

    model         = Contact
    template_name = 'ContactUsDelete.html'
    success_url   = '/contact-us/contactList/'