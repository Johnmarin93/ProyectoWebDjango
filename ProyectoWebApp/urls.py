from django.urls import include, path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.Home, name="Home"),
    path('Servicios/', include("Servicios.urls")),
    path('Blog/', include("Blog.urls")),
    path('Contacto/', include("Contacto.urls")),
    path('Tienda/', include("Tienda.urls")),
    path('carro/', include("carro.urls")),
    path('pedidos/', include("pedidos.urls")), 
    path('Autenticacion/', include("Autenticacion.urls")),

   

]

urlpatterns+=static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)