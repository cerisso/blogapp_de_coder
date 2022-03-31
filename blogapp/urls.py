from django.urls import path
from blogapp.views import *



urlpatterns = [
    path("", inicio, name = "inicio"),
    path("crypto/", cryptos, name = "crypto"),
    path("acciones/", acciones, name = "acciones"),
    path("formularioposteos/", formulario_posteos, name = "posteos"),


]
