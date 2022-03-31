from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from blogapp.forms import Crear_posteo





# Create your views here.
def inicio(request):
    date_init = datetime.now()
    hora = {"hora": "son las", "date_init": date_init }

    return render(request, "blogapp/base.html")

def posteos (request):
    return render(request, "blogapp/Posteos.html")

def cryptos (request):
    return render(request, "blogapp/Crypto.html")

def acciones (request):
    return render(request, "blogapp/Acciones.html")

def formulario_posteos (request):

    if request.method == "post":

        Posteo = Crear_posteo(request.post)
        
        if Posteo.is_valid:
            data = Posteo.cleaned_data

            nuevo_posteo = Posteo(data["titulo"],data["posteo"])
            nuevo_posteo.save()
        return render(request, "blogapp/index.html")

    else:
        posteo = formulario_posteos

    return render(request, "blogapp/Posteosformulario.html")



    




