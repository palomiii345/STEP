from django.shortcuts import render


def bienvenida(request):

    return render(request, 'bienvenida.html')


#menuu

def inicio(request):

    return render(request, 'inicio.html')


def servicios(request):
    return render(request, 'servicios.html')

def clientes(request):
    return render(request, 'clientes.html')

def contactos(request):
    return render(request, 'contactos.html')

def nosotros(request):

    return render(request, 'nosotros.html')



# Create your views here.


