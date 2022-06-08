from django.urls import path
# from obras.views import crear_obra, search_obra, buscar
from obras import views



urlpatterns = [
    path('crear-obra/', views.crear_obra, name='crear-obra'),
    path('listado_obras/', views.)
    path('search_obra/', views.search_obra, name='search_obra'),
    path('buscar/', views.buscar, name='buscar')
    ]