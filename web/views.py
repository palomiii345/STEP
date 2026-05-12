from django.shortcuts import render


def bienvenida(request):

    return render(request, 'bienvenida.html')


def inicio(request):

    return render(request, 'inicio.html')



# Create your views here.


