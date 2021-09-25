from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    autor = models.ForeignKey(User,on_delete=models.RESTRICT)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_created=True,default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)
    categoria = models.OneToOneField(Categoria,on_delete=models.RESTRICT,null=True)

    def __str__(self):
        return self.titulo