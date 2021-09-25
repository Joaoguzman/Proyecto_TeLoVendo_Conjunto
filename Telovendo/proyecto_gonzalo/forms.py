from .models import Proveedor
from django import forms

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=('nombre','apellido','telefono')



