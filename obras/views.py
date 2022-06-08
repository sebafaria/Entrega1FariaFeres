from django.shortcuts import render





def create_obra(request):
    return render(request, 'create_obra.html')
