from django.db import models

# Create your models here.
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

class Articulo(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    fecha = models.DateField()
    seccion = models.CharField(max_length=40, default="General") 

class Seccion(models.Model):
    nombre = models.CharField(max_length=30)