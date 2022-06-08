from django.db import models

# Create your models here.

class Obra(models.Model):
    cliente = models.CharField(max_length=100)
    nrocliente = models.FloatField()
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()

class Clientes(models.Model):
    nombrecliente = models.CharField(max_length=100)
    direccionfiscal = models.CharField(max_length=100)
    cuit = models.IntegerField()
    fechaingreso = models.DateField()
    antiguedad = models.IntegerField()

class Empleados(models.Model):
    nombreapellido = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    dni = models.IntegerField()
    fechaing = models.DateField()
    antig = models.IntegerField()