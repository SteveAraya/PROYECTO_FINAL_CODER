from django.urls import path

from App_ContactUs.views import (
    ContactUs,
)

urlpatterns = [    

    path('send-message', ContactUs,  name='ContactUs'),

]