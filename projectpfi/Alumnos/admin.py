from django.contrib import admin
from .models import Alumnos

# Register your models here.
@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombres', 'apellidos', 'matricula', 'carrera', 'correo','img')
    list_editable = ('nombres', 'apellidos', 'matricula', 'carrera', 'correo','img')
    list_filter = ('created', 'modified')