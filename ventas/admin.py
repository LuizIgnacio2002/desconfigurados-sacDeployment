from django.contrib import admin
from .models import *

class PagoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pago._meta.fields]
    ordering = ('fechahora_pago', 'monto',)

class OrdenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Orden._meta.fields]
    ordering = ('cliente', 'fechahora_orden',)

class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DetalleOrden._meta.fields]
    ordering = ('orden', 'producto',)

admin.site.register(Pago, PagoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(DetalleOrden, DetalleOrdenAdmin)