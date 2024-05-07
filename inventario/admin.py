from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Categoria._meta.fields]
    ordering = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Producto._meta.fields]
    ordering = ('nombre',)

class ResiduoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Residuo._meta.fields]
    ordering = ('nombre',)

class ContenedorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contenedor._meta.fields]
    ordering = ('producto', 'residuo',)



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Residuo, ResiduoAdmin)
admin.site.register(Contenedor, ContenedorAdmin)
