from django.urls import path
from obras.views import create_obra




urlpatterns = [
    path('create-obra/', create_obra, name='create-obra'),
    
    ]