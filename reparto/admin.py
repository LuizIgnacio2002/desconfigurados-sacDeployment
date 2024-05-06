from django.contrib import admin
from .models import *

class UbicacionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ubicacion._meta.fields]
    ordering = ('ciudad', 'direccion',)

class EntregaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entrega._meta.fields]
    ordering = ('ubicacion', 'empleado', 'fechahora_entrega',)

admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Entrega, EntregaAdmin)
