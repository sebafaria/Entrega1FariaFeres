from django.shortcuts import render
from obras.models import Obra
from obras.forms import Obra_form

def crear_obra(request):
    return render(request, 'crear_obra.html')

def search_obra(request):
    obra = Obra.objects.filter(name__icontains=request.GET['search'])
    if obra.exists():
        context={'obra':obra}
    else:
        context={'errors':'No se encontro la obra'}
    return render(request,'search_obra.html',context=context)