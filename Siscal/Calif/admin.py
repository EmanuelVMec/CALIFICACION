from django.contrib import admin
from .models import Estudiante, Materia, Docente, Nota
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Docente)
admin.site.register(Nota)
