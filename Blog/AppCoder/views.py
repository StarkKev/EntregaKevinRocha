from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from AppCoder.models import Videojuegos
from AppCoder.models import Hardware
from AppCoder.models import Plataformas
from AppCoder.forms import VideojuegosFormulario
from AppCoder.forms import HardwareFormulario
from AppCoder.forms import PlataformasFormulario

# Create your views here.
def videojuegos(request):
    if request.method == "POST":
            miFormulario = VideojuegosFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  videojuego = Videojuegos(nombre=informacion["videojuegos"], genero=informacion["genero"], ano_lanzamiento=informacion["ano_lanzamiento"])
                  videojuego.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = VideojuegosFormulario()

    return render(request, "AppCoder/videojuegos.html", {"miFormulario": miFormulario})

def hardware(request):
    if request.method == "POST":
            miFormulario = HardwareFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  hardware = Hardware(nombre=informacion["hardware"], distribuidor=informacion["distribuidor"], precio=informacion["precio"])
                  hardware.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = HardwareFormulario()
    return render(request, "AppCoder/hardware.html", {"miFormulario": miFormulario})

def plataformas(request):
    if request.method == "POST":
            miFormulario = PlataformasFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  hardware = Plataformas(nombre=informacion["plataformas"], precio=informacion["precio"], ano_lanzamiento=informacion["ano_lanzamiento"])
                  hardware.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = PlataformasFormulario()
    return render(request, "AppCoder/plataformas.html", {"miFormulario": miFormulario})

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def buscar(request):
    anolanzamiento_views = request.GET['ano_lanzamiento']
    videojuegos_todos = Videojuegos.objects.filter(ano_lanzamiento=anolanzamiento_views)
    return render(request,"AppCoder/resultadoVideojuegos.html",{"ano_lanzamiento":anolanzamiento_views,"videojuegos":videojuegos_todos})

def buscarvideojuegos(request):
    return render(request,'AppCoder/busquedavideojuegos.html')

def buscar2(request):
    distribuidor_views = request.GET['distribuidor']
    hardware_todos = Hardware.objects.filter(distribuidor=distribuidor_views)
    return render(request,"AppCoder/resultadoHardware.html",{"distribuidor":distribuidor_views,"hardware":hardware_todos})

def buscarhardware(request):
    return render(request,'AppCoder/busquedahardware.html')

def buscar3(request):
    nombre_views = request.GET['nombre']
    plataforma_todos = Plataformas.objects.filter(nombre=nombre_views)
    return render(request,"AppCoder/resultadoPlataforma.html",{"nombre":nombre_views,"plataforma":plataforma_todos})

def buscarplataforma(request):
    return render(request,'AppCoder/busquedaplataformas.html')