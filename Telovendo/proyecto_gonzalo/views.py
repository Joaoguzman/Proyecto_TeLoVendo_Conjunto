from Proyecto_TeLoVendo_Conjunto.Telovendo.proyecto_gonzalo.models import Proveedor
from django.shortcuts import redirect, render
from .forms import ProveedorForm

# Create your views here.

def agregar_proveedor(request):
    form=ProveedorForm()
    if request.method =='POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor')
    else:
        form=ProveedorForm(request.POST)
    context= {"form":form}
    return render(request,'proyecto_gonzalo/proveedor.html',context)
