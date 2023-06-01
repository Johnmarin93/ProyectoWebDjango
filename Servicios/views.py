from django.shortcuts import render
from Servicios.models import  Servicio


def Servicios(request):
    Servicios=Servicio.objects.all()
    return render(request, "Servicios/Servicios.html", {'Servicios': Servicios})
