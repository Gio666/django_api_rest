from django.db import models

# Create your models here.


# Clase cancion
class Cancion(models.Model):
    nombre = models.CharField(max_length=150)
    fecha = models.DateTimeField()
    duracion = models.CharField(max_length=10)
    album = models.CharField(max_length=150)
    artista = models.CharField(max_length=150)
    banda = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    subgenero = models.CharField(max_length=150)
    similares = models.CharField(max_length=255)
    labels = models.CharField(max_length=255)
    instrumentos = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
