from django.urls import path
from App_proyectoWeb import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('tienda/', views.tienda, name='tienda'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
]