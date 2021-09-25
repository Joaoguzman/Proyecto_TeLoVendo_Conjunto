from django.shortcuts import render,get_object_or_404
from .models import Entrada,Categoria
# Create your views here.

def listar_entradas(request):
    entradas = Entrada.objects.all()   
    return render(request,'blog/entrada/listar.html',{'entradas':entradas})

def detalle_entrada(request,id):
    entrada = get_object_or_404(Entrada,pk=id)  
    return render(request,'blog/entrada/detalle.html',{'entrada':entrada})

