from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
path('', views.Blog, name="Blog"),
path('Categoria/<int:categoria_id>/', views.categoria, name="Categoria")
]
