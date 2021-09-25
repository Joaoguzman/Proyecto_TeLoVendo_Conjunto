from .models import Biblioteca
from django import forms

class BibliotecaForm(forms.ModelForm):
    
    class Meta:
        model = Biblioteca
        fields = ('nombre','autor','fecha_publicacion')
