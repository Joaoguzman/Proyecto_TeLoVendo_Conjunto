from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Comentario(models.Model):
    proveedor = models.CharField(max_length=50)
    contenido = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.name}\n{self.contenido}'
    