
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("App_MVTProyectoFinalCoder.urls")),
    path('blog/', include("App_Blog.urls")),
    path('car/', include("App_Car.urls")),
    path('contact-us/', include("App_ContactUs.urls")),
    path('login/', include("App_Login.urls")),
    path('office/', include("App_Office.urls")),
    path('register/', include("App_Register.urls")),
    path('reservation/', include("App_Reservation.urls")),
]
