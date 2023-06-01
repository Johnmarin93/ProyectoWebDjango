from django.shortcuts import render, HttpResponse

from carro.carro import Carro



def Home(request):
    #carro=Carro(request)
    return render(request, "ProyectoWebApp/Home.html")









