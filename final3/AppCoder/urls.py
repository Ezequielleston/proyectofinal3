from django.urls import path
from .views import crear_autos, listar_autos, camionetas, motos, autos, buscarAuto, buscar, buscar2, buscarCamioneta,buscar3, buscarMoto, inicio

urlpatterns = [
    path("crear_autos/", crear_autos),
    path("listar_autos/", listar_autos),
    path("camionetas/", camionetas, name="camionetas"),
    path("motos/", motos, name="motos"),
    path("autos/", autos, name="autos"),
    path("buscarAuto/", buscarAuto, name="buscarAuto"),
    path("buscar/",buscar, name="buscar"),
    path("buscar2/",buscar2, name="buscar2"),
    path("buscarCamioneta/", buscarCamioneta, name="buscarCamioneta"),
    path("buscar3/",buscar3, name="buscar3"),
    path("buscarMoto/", buscarMoto, name="buscarMoto"),

]