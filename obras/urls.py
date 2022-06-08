from django.urls import path
from obras.views import crear_obra, search_obra




urlpatterns = [
    path('crear-obra/', crear_obra, name='crear-obra'),
    path('search_products/', search_obra, name='search_obra')
    ]