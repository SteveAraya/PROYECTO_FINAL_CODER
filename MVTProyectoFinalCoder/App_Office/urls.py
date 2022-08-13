from django.urls import path

from App_Office.views import (
    OfficeCreate,
)

urlpatterns = [    

    path('create', OfficeCreate,  name='OfficeCreate'),

]