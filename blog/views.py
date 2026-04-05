from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Autor, Articulo, Seccion, Avatar, Perfil
from .forms import AutorFormulario, ArticuloFormulario, SeccionFormulario
from .forms import RegistroFormulario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroFormulario
from .forms import UserEditForm

def inicio(request):
    return render(request, "blog/inicio.html")

@login_required
def autor_formulario(request):
    if request.method == "POST":
        mi_formulario = AutorFormulario(request.POST) 
        
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            
            # Creamos el objeto Autor con la info que escribió el usuario
            nuevo_autor = Autor(
                nombre=info['nombre'], 
                apellido=info['apellido'], 
                profesion=info['profesion']
            )
            nuevo_autor.save() # ¡Acá se guarda en la base de datos!
            
            return render(request, "blog/inicio.html") 
    else:
        mi_formulario = AutorFormulario() # Si no es POST, mostramos el form vacío
    
    return render(request, "blog/autor_formulario.html", {"mi_formulario": mi_formulario})

@login_required
def articulo_formulario(request):
    if request.method == "POST":
        # 🔴 AGREGAMOS request.FILES para recibir la imagen
        form = ArticuloFormulario(request.POST, request.FILES) 
        
        if form.is_valid():
            info = form.cleaned_data
            nuevo_articulo = Articulo(
                titulo=info['titulo'], 
                texto=info['texto'], 
                fecha=info['fecha'],
                seccion=info['seccion'],
                imagen=info.get('imagen') 
            )
            
            nuevo_articulo.save() 
            return render(request, "blog/inicio.html", {"mensaje": "¡Artículo creado con éxito!"})
    else:
        form = ArticuloFormulario()
    
    return render(request, "blog/articulo_formulario.html", {"mi_formulario": form})

# Vista para Secciones
@login_required
def seccion_formulario(request):
    if request.method == "POST":
        form = SeccionFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nuevo = Seccion(nombre=info['nombre'])
            nuevo.save()
            return render(request, "blog/inicio.html")
    else:
        form = SeccionFormulario()
    return render(request, "blog/seccion_formulario.html", {"mi_formulario": form})

def buscar(request):
    criterio = request.GET.get('criterio', '').strip()
    todos_los_articulos = None # Variable auxiliar
    
    if criterio:
        articulos = Articulo.objects.filter(titulo__icontains=criterio)
        # 💡 Si buscó algo y NO hubo resultados, cargamos TODOS para ofrecerlos abajo
        if not articulos.exists():
            todos_los_articulos = Articulo.objects.all()
    else:
        # Si no escribió nada, articulos ya son todos
        articulos = Articulo.objects.all()

    return render(request, "blog/resultados_busqueda.html", {
        "articulos": articulos, 
        "criterio": criterio,
        "sugeridos": todos_los_articulos # Pasamos los sugeridos si la búsqueda falló
    })

# Vista para EDITAR (Update)
class ArticuloUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = "blog/articulo_editar.html"
    fields = ['titulo', 'texto', 'seccion', 'fecha', 'imagen'] 
    success_url = reverse_lazy('blog:Inicio')

# Vista para BORRAR (Delete)
class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = "blog/articulo_borrar.html"
    success_url = reverse_lazy('blog:Inicio')

# Vista de Registro
def registro(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            user = form.save() # Guardamos el usuario (la llave)
            rol_elegido = form.cleaned_data.get('rol')
            
            # Creamos el Perfil asociado automáticamente
            # (Asumiendo que ya creaste el modelo Perfil en models.py)
            Perfil.objects.create(user=user, rol=rol_elegido)
            
            return render(request, "blog/inicio.html", {"mensaje": "¡Registro exitoso! Ya podés loguearte."})
    else:
        form = RegistroFormulario()
        
    return render(request, "blog/registro.html", {"form": form})

# El login lo manejaremos por URL (más fácil), pero necesitamos el Logout aquí:
def desloguear(request):
    logout(request)
    return render(request, "blog/inicio.html", {"mensaje": "Sesión cerrada correctamente"})

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        # Importante: request.FILES es para la imagen
        imagen = request.FILES.get('imagen')
        if imagen:
            # Borramos avatares viejos del usuario
            Avatar.objects.filter(user=request.user).delete()
            # Guardamos el nuevo
            nuevo_avatar = Avatar(user=request.user, imagen=imagen)
            nuevo_avatar.save()
            return render(request, "blog/inicio.html", {"mensaje": "¡Avatar actualizado!"})
            
    return render(request, "blog/agregar_avatar.html")

@login_required
def editar_perfil(request):
    usuario = request.user
    # 🔴 BUSCAMOS EL AVATAR ACTUAL
    avatar = Avatar.objects.filter(user=usuario).first()
    url_avatar = avatar.imagen.url if avatar else None

    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST, instance=usuario)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return render(request, "blog/inicio.html", {"mensaje": "¡Perfil actualizado!"})
    else:
        mi_formulario = UserEditForm(instance=usuario)

    return render(request, "blog/editar_perfil.html", {
        "mi_formulario": mi_formulario,
        "url_avatar": url_avatar # 🔴 LE PASAMOS LA URL DE LA FOTO
    })

def about(request):
    return render(request, 'blog/about.html')
# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Articulo

# Esta es la función que te faltaba:
def detalle_articulo(request, pk):
    # Buscamos el artículo por su ID (pk) o tiramos un error 404 si no existe
    articulo = get_object_or_404(Articulo, id=pk)
    
    return render(request, "blog/detalle_articulo.html", {"articulo": articulo})