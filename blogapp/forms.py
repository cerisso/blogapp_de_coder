from django import forms


class Crear_posteo (forms.Form):

    titulo = forms.CharField(max_length=50)
    posteo = forms.CharField(max_length=500)

