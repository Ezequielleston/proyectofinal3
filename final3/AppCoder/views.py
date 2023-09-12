from django.shortcuts import render
from .models import Autos, Camionetas, Motos
from .forms import Autosform, Camionetasform, Motosform
from django.http import HttpResponse

# Create your views here.

def crear_autos(request):
    
    marca_autos="honda"
    modelo_autos="civic"
    print("Buscando tu vehiculo")
    autos=Autos(marca=marca_autos,modelo=modelo_autos)
    autos.save()
    respuesta=f"Tu vehiculo: {autos.marca} - {autos.modelo}"
    return HttpResponse(respuesta)
def listar_autos(request):
    autos=Autos.objects.all()
    respuesta=""
    for autos in Autos:
        respuesta+=f"{autos.marca} - {autos.modelo}<br>"
    return HttpResponse(respuesta)
        


def inicio(request):
    return render(request,"AppCoder/inicio.html")


def camionetas(request):
    if request.method=="POST":
        form=Camionetasform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca=info["marca"]
            modelo=info["modelo"]
            camionetas=Camionetas(marca=marca,modelo=modelo)
            camionetas.save()
            return render(request,"AppCoder/CAMIONETAS.html", {"mensaje":"Camioneta creada"})
        else:
            return render(request,"AppCoder/CAMIONETAS.html", {"mensaje": "Datos invalidos"})
    else:    

        formulario_camionetas=Camionetasform()
        return render(request,"AppCoder/CAMIONETAS.html", {"formulario":formulario_camionetas})
    
def motos(request):
    if request.method=="POST":
        form=Motosform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca=info["marca"]
            modelo=info["modelo"]
            motos=Motos(marca=marca,modelo=modelo)
            motos.save()
            return render(request,"AppCoder/MOTOS.html", {"mensaje":"Moto creada"})
        else:
            return render(request,"AppCoder/MOTOS.html", {"mensaje": "Datos invalidos"})
    else:    
        formulario_motos=Motosform()
        return render(request,"AppCoder/MOTOS.html", {"formulario":formulario_motos})
    

def autos(request):
    if  request.method=="POST":
        form=Autosform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca=info["marca"]
            modelo=info["modelo"]
            autos=Autos(marca=marca,modelo=modelo)
            autos.save()
            return render(request,"AppCoder/AUTOS.html", {"mensaje": "Auto creado"})
        return render(request,"AppCoder/AUTOS.html", {"mensaje": "Datos invalidos"})
    else:
        formulario_autos=Autosform()
        return render(request,"AppCoder/AUTOS.html", {"formulario": formulario_autos})


def buscarAuto(request):
    return render(request,"AppCoder/buscarAuto.html")

def buscar(request):
    modelo=request.GET["modelo"]
    if modelo!="":
        autos=Autos.objects.filter(modelo=modelo)
        return render(request, "AppCoder/resultadoAuto.html", {"autos":autos})
    else:
        return render(request, "AppCoder/buscarAuto.html", {"mensaje":"no ingresaste nada"})


def buscarCamioneta(request):
        return render(request,"AppCoder/buscarCamioneta.html")

def buscar2(request):
    modelo=request.GET["modelo"]
    if modelo!="":
        camionetas=Camionetas.objects.filter(modelo=modelo)
        return render(request, "AppCoder/resultadoCamioneta.html", {"camionetas":camionetas})
    else:
        return render(request, "AppCoder/buscarCamioneta.html", {"mensaje":"no ingresaste nada"})


def buscarMoto(request):
    return render(request,"AppCoder/buscarMoto.html")

def buscar3(request):
    modelo=request.GET["modelo"]
    if modelo!="":
        motos=Motos.objects.filter(modelo=modelo)
        return render(request, "AppCoder/resultadoMoto.html", {"motos":motos})
    else:
        return render(request, "AppCoder/buscarMoto.html", {"mensaje":"no ingresaste nada"})