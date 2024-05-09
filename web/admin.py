from django.contrib import admin
from .models import *



class UsuarioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Usuario._meta.fields]
    ordering = ('username',)

admin.site.register(Usuario, UsuarioAdmin)
