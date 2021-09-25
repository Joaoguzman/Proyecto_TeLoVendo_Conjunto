from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.agregar_libro, name='formulario'),
]
