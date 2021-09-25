from django.urls import path 
from . import views

urlpatterns = [
    path('proveedor/',views.agregar_proveedor,name="proveedor")
]