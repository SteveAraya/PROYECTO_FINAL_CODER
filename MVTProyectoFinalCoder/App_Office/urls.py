from django.urls import path

from App_Office.views import (
    OfficeCreate,
    OfficeList,
    OfficeDelete,
    OfficeListHome,
)

urlpatterns = [    

    path('officeCreate/', OfficeCreate.as_view(), name="OfficeCreate"),
    path('officeList/', OfficeList.as_view(), name="OfficeList"),
    path('officeDelete/<int:pk>', OfficeDelete.as_view(), name="OfficeDelete"),
    path('officeListHome/', OfficeListHome.as_view(), name="OfficeListHome"),

]