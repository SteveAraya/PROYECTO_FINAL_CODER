from django.urls import path

from .views import PostCreate, PostDelete, PostDetail, PostList, PostTable, PostUpdate

urlpatterns = [    

    path('create/', PostCreate,  name='PostCreate'),
    path('table/', PostTable,  name='PostTable'),
    path('list/', PostList,  name='PostList'),
    path('detail/<int:id>', PostDetail,  name='PostDetail'),
    path('edit/<pk>', PostUpdate.as_view(),  name='PostEdit'),
    path('delete/<pk>', PostDelete.as_view(),  name='PostDelete'),

]