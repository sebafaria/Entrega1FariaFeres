from multiprocessing.connection import Client
from django.contrib import admin
from obras.models import Obra
from obras.models import Clientes
from obras.models import Empleados

# Register your models here.

admin.site.register(Obra)
admin.site.register(Clientes)
admin.site.register(Empleados)