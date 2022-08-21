from django.urls import path

from App_ContactUs.views import (
    ContactUS,
    ContactUsList,
    ContactUsDelete,
)

urlpatterns = [    

    path('sendMessage/', ContactUS,  name='SendMessage'),
    path('contactList/', ContactUsList.as_view(), name="ContactUsList"),
    path('contactUsDelete/<int:pk>', ContactUsDelete.as_view(), name="ContactUsDelete"),

]