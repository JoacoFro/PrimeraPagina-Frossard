from django.contrib import admin
from .models import Perfil, Autor, Articulo, Seccion, Avatar

# Registramos los modelos para que aparezcan en el panel /admin
admin.site.register(Perfil)
admin.site.register(Autor)
admin.site.register(Articulo)
admin.site.register(Seccion)
admin.site.register(Avatar)