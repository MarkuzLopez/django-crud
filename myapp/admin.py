from django.contrib import admin
from .models import Estudiante, Curso

# Register your models here.
# Relaciones entre modelos (OneToMany, ManyToMany) con admin y formularios.

# Relaciones entre modelos (OneToMany, ManyToMany) con admin y formularios.
# paso2 registrar en el admin
admin.site.register(Estudiante)
admin.site.register(Curso)