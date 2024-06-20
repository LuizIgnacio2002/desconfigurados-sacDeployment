from django.db import models
from configuracion.models import *
from web.models import *

class Ubicacion(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE, verbose_name = "Ciudad")
    direccion = models.CharField("Dirección", max_length = 1000)
    referencia = models.CharField("Referencia", max_length = 500)
    codigo_postal = models.CharField("Código postal", max_length = 20)
    latitud = models.DecimalField("Latitud", max_digits = 12, decimal_places = 8)
    longitud = models.DecimalField("Longitud", max_digits = 12, decimal_places = 8)
    def __str__(self):
        return f"{self.ciudad} {self.direccion}"
    class Meta:
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"
        db_table = "Ubicacion"

class Entrega(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete = models.CASCADE, blank = True, null = True, verbose_name = "Orden")
    empleado = models.ForeignKey(Usuario, on_delete = models.CASCADE,  blank = True, null = True, verbose_name = "Empleado asignado")
    fechahora_entrega = models.DateTimeField("Fecha y hora de entrega", auto_now_add = True)
    detalles_entrega = models.CharField("Anotaciones del encargado de la entrega", max_length = 1000, blank = True, null = True)
    estado_entrega = models.ForeignKey(EstadoEntrega, on_delete = models.CASCADE, verbose_name = "Estado de la entrega")
    def __str__(self):
        return f"{self.ubicacion} {self.empleado} {self.fechahora_entrega}"
    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"
        db_table = "Entrega"

