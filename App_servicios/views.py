from django.shortcuts import render
from App_servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servicios})