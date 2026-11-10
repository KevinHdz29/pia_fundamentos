from django.shortcuts import render
from .models import Producto, Servicio

# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def catalogo(request):
    datos = {
        'productos': Producto.objects.all(),
        'servicios': Servicio.objects.all()
    }
    return render(request, 'catalogo.html', context=datos)


def cortes(request):
    return render(request, 'cortes.html')


def personal(request):
    return render(request, 'personal.html')


def contacto(request):
    return render(request, 'contacto.html')