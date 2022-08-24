from django.urls import path

from App_Register.views import (
    Register,
)

urlpatterns = [    

    path('createUser', Register,  name='Register'),

]