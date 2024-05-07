from django.contrib import admin
from .models import *

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TipoDocumento._meta.fields]
    ordering = ('nombre',)

class PaisAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pais._meta.fields]
    ordering = ('nombre',)

class CiudadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ciudad._meta.fields]
    ordering = ('nombre',)

class EstadoEntregaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EstadoEntrega._meta.fields]
    ordering = ('nombre',)

class EstadoOrdenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EstadoOrden._meta.fields]
    ordering = ('nombre',)

admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(EstadoEntrega, EstadoEntregaAdmin)
admin.site.register(EstadoOrden, EstadoOrdenAdmin)
