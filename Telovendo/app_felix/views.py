from Proyecto_TeLoVendo_Conjunto.Telovendo.app_felix.models import Comentario
from django.shortcuts import render, redirect
from .forms import ComentariosForm

# Create your views here.

#Falta terminar el bucle

def comentarios(request):
    #comentarios = Comentario.objects.all()
    if request.method == 'POST':
        form_comentarios = ComentariosForm(request.POST)
        if form_comentarios.is_valid():
            form_comentarios.save()
            return redirect('comentarios')
    else:
        form_comentarios = ComentariosForm()

    contexto = {'form_comentarios': form_comentarios}

    return render(request, 'app_felix/comentarios.html', contexto)