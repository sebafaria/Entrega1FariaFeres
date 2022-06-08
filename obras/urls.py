from django.urls import path
from obras.views import crear_obra




urlpatterns = [
    path('crear-obra/', crear_obra, name='crear-obra'),
    
    ]