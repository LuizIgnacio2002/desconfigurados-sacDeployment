from django.db import models

from web.models import *
from inventario.models import *
from reparto.models import *

class Pago(models.Model):
    monto = models.DecimalField("Monto total", max_digits = 16 , decimal_places = 2)
    fechahora_pago = models.DateTimeField("Fecha y hora de pago", auto_now_add = True)
    def __str__(self):
        return f"{self.fecha_pago} {self.monto}"
        #return str(self.fecha_pago)
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        db_table = "Pago"

class Orden(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete = models.CASCADE, verbose_name = "Cliente")
    fechahora_orden = models.DateTimeField("Fecha y hora de registro del orden", auto_now_add = True)
    pago = models.ForeignKey(Pago, on_delete = models.CASCADE, blank = True, null = True, verbose_name = "Pago")
    entrega = models.ForeignKey(Entrega, on_delete = models.CASCADE, blank = True, null = True, verbose_name = "Entrega")
    estado_orden = models.ForeignKey(EstadoOrden, on_delete = models.CASCADE, verbose_name = "Estado de la orden")
    def __str__(self):
        return f"{self.cliente} {self.fechahora_orden}"
    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        db_table = "Orden"

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete = models.CASCADE, verbose_name = "Orden")
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE, verbose_name = "Producto")
    cantidad = models.IntegerField("Cantidad")
    def __str__(self):
        return f"{self.orden} {self.producto}"
        #return self.orden
    class Meta:
        verbose_name = "Detalle orden"
        verbose_name_plural = "Detalles orden"
        db_table = "DetalleOrden"