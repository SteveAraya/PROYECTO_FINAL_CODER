from django.urls import path

from App_Register.views import (
    Register,
    UserEdit,
    AddAvatar,
    UserList,
)

urlpatterns = [    

    path('createUser', Register,  name='Register'),
    path('useredit', UserEdit, name= "UserEdit"),
    path('addavatar', AddAvatar, name= "AddAvatar"),
    path('userList/', UserList.as_view(), name="UserList"),

]