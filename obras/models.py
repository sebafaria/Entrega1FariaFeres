from django.db import models
from django.utils.timezone import now
# Create your models here.

class Obra(models.Model):
    cliente = models.CharField(max_length=100)
    nrocliente = models.FloatField()
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(default=now)


    def __str__(self):
        return f"Cliente: {self.cliente} - Numero de cliente {self.nrocliente} - Obra: {self.nombre} - Fecha: {self.fecha}"

class Clientes(models.Model):
    nombrecliente = models.CharField(max_length=100)
    direccionfiscal = models.CharField(max_length=100)
    cuit = models.IntegerField()
    fechaingreso = models.DateField(default=now)
    antiguedad = models.IntegerField()

class Empleados(models.Model):
    nombreapellido = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    dni = models.IntegerField()
    fechaing = models.DateField(default=now)
    antig = models.IntegerField()