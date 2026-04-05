from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Articulo

class RegistroFormulario(UserCreationForm):
    # Definimos las opciones que verá el usuario
    ROLES = [
        ('lector', 'Solo Lector (Ver y buscar)'),
        ('autor', 'Autor (Cargar servicios y artículos)'),
    ]
    
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(choices=ROLES, label="¿Qué perfil deseás tener?")

    class Meta:
        model = User
        fields = ['username', 'email', 'rol']
        
class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)

from django import forms

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    seccion = forms.CharField(max_length=40) 
    texto = forms.CharField(widget=forms.Textarea) 
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    imagen = forms.ImageField(
        label="Imagen del Artículo", 
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    
class SeccionFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
        }