from django.shortcuts import render
from .carro import Carro
from Tienda.models import Producto
from django.shortcuts import redirect

def agregar_producto(request, producto_id):
    car=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    car.agregar(producto=producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiear_carro()
    return redirect("Tienda")


# Create your views here.

 