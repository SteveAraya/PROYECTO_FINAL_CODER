
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404

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

handler404 = 'App_MVTProyectoFinalCoder.views.PageNotFound'

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)