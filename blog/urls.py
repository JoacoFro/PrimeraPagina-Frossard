from django.urls import path
from . import views  # Importamos las vistas de tu app blog
from django.contrib.auth.views import LoginView, LogoutView # Importamos las vistas de Django
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    # Inicio y formularios básicos
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name='About'), 
    path('autor-formulario/', views.autor_formulario, name="AutorFormulario"),
    path('articulo-formulario/', views.articulo_formulario, name="ArticuloFormulario"),
    path('seccion-formulario/', views.seccion_formulario, name="SeccionFormulario"),
    
    
    # Buscador
    path('buscar/', views.buscar, name="Buscar"),
    
    # CRUD (Editar y Borrar)
    path('editar-articulo/<int:pk>/', views.ArticuloUpdate.as_view(), name="ArticuloEditar"),
    path('borrar-articulo/<int:pk>/', views.ArticuloDelete.as_view(), name="ArticuloBorrar"),

    # Usuarios (Login, Registro, Logout)
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('registro/', views.registro, name="Registro"),
    
    # Perfil (Avatar)
    path('agregar-avatar/', views.agregar_avatar, name="AgregarAvatar"),
    path('editar-perfil/', views.editar_perfil, name='EditarPerfil'),
    
    # Cambiar Password
    path('password/', auth_views.PasswordChangeView.as_view(
    template_name='blog/cambiar_password.html', 
    success_url='/pages/editar-perfil/' 
), name='CambiarPassword'),
]