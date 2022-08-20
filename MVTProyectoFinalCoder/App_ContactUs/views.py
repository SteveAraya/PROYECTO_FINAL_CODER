from django.http          import HttpResponse
from django.shortcuts     import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from App_MVTProyectoFinalCoder.models import Contact
from App_MVTProyectoFinalCoder.forms  import ContactUsForm

# Create your views here.

#------------------- ContactUS VIEWS -------------------#
def SendMessage(self):
    
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
            return render(self,'ContactUS.html')

    else:
        return render(self, "ContactUS.html")

class ContactUsList(ListView):

    model               = Contact
    template_name       = './ContactUsList.html'
    context_object_name = 'ContactList'