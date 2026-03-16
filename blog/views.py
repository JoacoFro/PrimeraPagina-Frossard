from django.shortcuts import render
from blog.forms import AutorFormulario, ArticuloFormulario, SeccionFormulario
from blog.models import Autor, Seccion          # Importamos el modelo para guardar datos
from blog.models import Autor, Articulo, Seccion

# Esta es la que ya tenías
def inicio(request):
    return render(request, "blog/inicio.html")

# ESTA ES LA NUEVA (Punto 2)
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
# Vista para Artículos
# Así debería verse tu función en views.py
def articulo_formulario(request):
    if request.method == "POST":
        form = ArticuloFormulario(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            # Creamos el objeto incluyendo el nuevo campo 'seccion'
            nuevo_articulo = Articulo(
                titulo=info['titulo'], 
                texto=info['texto'], 
                fecha=info['fecha'],
                seccion=info['seccion']  # <--- Agregado
            )
            
            nuevo_articulo.save() 
            
            # Redirigimos al inicio después de guardar con éxito
            return render(request, "blog/inicio.html", {"mensaje": "¡Artículo creado con éxito!"})
    else:
        # Si el usuario solo entra a la página, enviamos el formulario vacío
        form = ArticuloFormulario()
    
    return render(request, "blog/articulo_formulario.html", {"mi_formulario": form})

# Vista para Secciones
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
    # Verificamos si el usuario envió algo en el campo "titulo"
    if request.GET.get("titulo"):
        titulo_buscado = request.GET["titulo"]
        
        # Buscamos artículos que CONTENGAN ese título (icontains ignora mayúsculas/minúsculas)
        articulos_encontrados = Articulo.objects.filter(titulo__icontains=titulo_buscado)

        return render(request, "blog/resultados_busqueda.html", {
            "articulos": articulos_encontrados, 
            "query": titulo_buscado
        })
    
    # Si no envió nada, simplemente mostramos la página del buscador
    return render(request, "blog/buscar.html")