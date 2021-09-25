from django.db import models


# Create your models here.

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(blank=True)

    def __str__(self):
        return self.nombre
