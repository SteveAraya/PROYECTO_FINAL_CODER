from django.urls import path

from App_Blog.views import (
    BlogCreate,
)

urlpatterns = [    

    path('create', BlogCreate,  name='BlogCreate'),

]