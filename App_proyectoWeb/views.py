from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'App_proyectoWeb/home.html')

def servicios(request):

    return render(request, 'App_proyectoWeb/servicios.html')

def tienda(request):

    return render(request, 'App_proyectoWeb/tienda.html')

def blog(request):

    return render(request, 'App_proyectoWeb/blog.html')

def contacto(request):

    return render(request, 'App_proyectoWeb/contacto.html')