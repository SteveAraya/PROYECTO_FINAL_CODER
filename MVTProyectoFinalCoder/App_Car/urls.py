from django.urls import path

from App_Car.views import (
    CarCreate,CarTable,CarList,CarDelete,CarDetail,CarUpdate,

)

urlpatterns = [    
    path('create/', CarCreate,  name='CarCreate'),
    path('table/', CarTable,  name='CarTable'),
    path('list/', CarList,  name='CarList'),
    path('detail/<int:id>', CarDetail,  name='CarDetail'),
    path('edit/<pk>', CarUpdate.as_view(),  name='CarEdit'),
    path('delete/<pk>', CarDelete.as_view(),  name='CarDelete'),
]