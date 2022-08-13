from django.urls import path

from App_Login.views import (
    Login,
)

urlpatterns = [    

    path('', Login,  name='Login'),

]