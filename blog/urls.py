from django.urls import path
from blog import views  # Importamos tus funciones de views.py

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor-formulario/', views.autor_formulario, name="AutorFormulario"),
    path('articulo-formulario/', views.articulo_formulario, name="ArticuloFormulario"),
    path('seccion-formulario/', views.seccion_formulario, name="SeccionFormulario"),
    path('buscar/', views.buscar, name="Buscar"), # La ruta para el buscador
    path('buscar/', views.buscar, name="Buscar"),
]