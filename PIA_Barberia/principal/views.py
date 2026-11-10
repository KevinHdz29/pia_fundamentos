from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def catalogo(request):
    return render(request, 'catalogo.html')


def cortes(request):
    return render(request, 'cortes.html')


def personal(request):
    return render(request, 'personal.html')


def contacto(request):
    return render(request, 'contacto.html')