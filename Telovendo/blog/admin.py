from django.contrib import admin
from .models import Categoria,Entrada
# Register your models here.

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('autor',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
   
