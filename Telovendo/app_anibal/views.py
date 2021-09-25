from django.shortcuts import render, redirect
from .forms import BibliotecaForm
# Create your views here.

def agregar_libro(request):
    if request.method=="POST":
        form=BibliotecaForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('formulario')
    else:
        form = BibliotecaForm() 


    context = {'form':form}

    return render(request, 'app_anibal/formulario.html', context)