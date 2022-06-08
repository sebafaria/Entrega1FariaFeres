from django.shortcuts import render
from obras.models import Obra
from obras.forms import Obra_form
from django.http import HttpResponse
def crear_obra(request):
    return render(request, 'crear_obra.html')

#def search_obra(request):
#    obra = Obra.objects.filter(name__icontains=request.GET['search'])
#    if obra.exists():
#        context={'obra':obra}
#    else:
#        context={'errors':'No se encontro la obra'}
#    return render(request,'search_obra.html',context=context)

def search_obra(request):

    return render(request,'search_obra.html')

def listado_obras(request)
    
    return render(request,'listado_obras.html')

def buscar(request):
    #respuesta = f"Estoy buscando la obra nro: {request.GET['nrocliente']}"

    if request.GET['nrocliente']:
        nrocliente = request.GET['nrocliente']
        nombre = Obra.objects.filter(nrocliente__icontains=nrocliente)
        return render(request,'resultadosbusqueda.html', {"nrocliente":nrocliente, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)