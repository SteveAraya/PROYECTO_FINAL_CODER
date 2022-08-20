from django.urls import path

from App_ContactUs.views import (
    SendMessage,
    ContactUsList,
)

urlpatterns = [    

    path('sendMessage', SendMessage,  name='SendMessage'),
    path('contactList/', ContactUsList.as_view(), name="ContactUsList"),

]