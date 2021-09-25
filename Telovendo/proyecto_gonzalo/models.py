from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.CharField(max_length=25)
    tipo_de_producto=models.CharField(max_length=50)
