from django.shortcuts import render, HttpResponse
from App_servicios.models import Servicio

# Create your views here.

def home(request):

    return render(request, 'App_proyectoWeb/home.html')

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, 'App_proyectoWeb/servicios.html', {'servicios': servicios})

def tienda(request):

    return render(request, 'App_proyectoWeb/tienda.html')

def blog(request):

    return render(request, 'App_proyectoWeb/blog.html')

def contacto(request):

    return render(request, 'App_proyectoWeb/contacto.html')