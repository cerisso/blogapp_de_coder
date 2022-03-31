from django.db import models

# Create your models here.
class Posteos(models.Model):

    titulo = models.CharField(max_length=50)
    posteo = models.TextField()


class Crypto(models.Model):

    ticker = models.CharField(max_length=10)
    valor = models.IntegerField()

class Acciones(models.Model):

    ticker = models.CharField(max_length=10)
    valor = models.IntegerField()