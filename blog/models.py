from django.db import models
from django.contrib.auth.models import User

# 1. PERFIL DE USUARIO (Unificado y con los campos de la consigna)
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agregamos biografia para cumplir con los requisitos base
    biografia = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    
    ROLES = [
        ('lector', 'Solo Lector'),
        ('autor', 'Autor / Creador'),
    ]
    rol = models.CharField(max_length=10, choices=ROLES, default='lector')

    def __str__(self):
        return f"{self.user.username} - {self.rol}"

# 2. MODELO PRINCIPAL (Con todos los campos mínimos pedidos)
class Articulo(models.Model):
    # 2 CharFields (Titulo y Seccion) - CHECK
    titulo = models.CharField(max_length=30)
    seccion = models.CharField(max_length=40, default="General")
    subtitulo = models.CharField(max_length=50, null=True, blank=True)
    
    # Texto (TextField) - CHECK
    texto = models.TextField() 
    
    # Fecha - CHECK
    fecha = models.DateField()
    
    # Imagen (Requisito base del modelo principal) - CHECK
    imagen = models.ImageField(upload_to='articulos', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"

# 3. OTROS MODELOS
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

class Seccion(models.Model):
    nombre = models.CharField(max_length=30)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"