from django.db import models

# Create your models here.

class Obra(models.Model):
    cliente = models.CharField(max_length=100)
    nrocliente = models.FloatField()
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()

