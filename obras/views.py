from django.shortcuts import render
from obras.models import Obra
from obras.forms import Obra_form
from django.http import HttpResponse
from django.views.generic import ListView

def crear_obra(request):
    if request.method == 'GET':
        form = Obra_form()
        context =  {'form': form}
        return render(request, 'crear_obra.html', context = context)
    else:
        form = Obra_form(request.POST)
        if form.is_valid():
            new_obra = Obra.objects.create(
                 cliente = form.cleaned_data [' cliente '],
                nrocliente = form.cleaned_data [' nrocliente '],
                nombre = form.cleaned_data [' nombre '],
                fecha = form.cleaned_data [' fecha '],
            )
            contexto = {'new_obra':new_obra}
        return render(request, 'crear_obra.html', context = contexto) 
#def search_obra(request):
#    obra = Obra.objects.filter(name__icontains=request.GET['search'])
#    if obra.exists():
#        context={'obra':obra}
#    else:
#        context={'errors':'No se encontro la obra'}
#    return render(request,'search_obra.html',context=context)

def search_obra(request):

    return render(request,'search_obra.html')

def listar_obras(request):
    lista_obras = Obra.objects.all()
    contextoo = {'listado_obras':lista_obras}
    return render(request,'listado_obras.html', context=contextoo)

def buscar(request):
    #respuesta = f"Estoy buscando la obra nro: {request.GET['nrocliente']}"

    if request.GET['nrocliente']:
        nrocliente = request.GET['nrocliente']
        nombre = Obra.objects.filter(nrocliente__icontains=nrocliente)
        return render(request,'resultadosbusqueda.html', {"nrocliente":nrocliente, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)