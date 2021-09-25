from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.listar_entradas,name='blog_listar_entradas'),
    path('<int:id>',views.detalle_entrada,name='blog_detalle_entrada'),
]