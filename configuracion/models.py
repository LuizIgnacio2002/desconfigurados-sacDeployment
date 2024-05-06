from django.db import models

class TipoDocumento(models.Model):
    nombre = models.CharField("Nombre", max_length = 100)
    descripcion = models.CharField("Descripción", max_length = 500)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"

class Pais(models.Model):
    nombre = models.CharField("Nombre", max_length = 100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

class Ciudad(models.Model):
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE, verbose_name = "País")
    nombre = models.CharField("Nombre", max_length = 100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class EstadoEntrega(models.Model):
    nombre = models.CharField("Nombre", max_length = 100)
    descripcion = models.CharField("Descripción", max_length = 500)
    def __str__(self):
        return f"{self.nombre}"
    class Meta:
        verbose_name = "Estado de la entrega"
        verbose_name_plural = "Estados de la entrega"

class EstadoOrden(models.Model):
    nombre = models.CharField("Nombre", max_length = 100)
    descripcion = models.CharField("Descripción", max_length = 500)
    def __str__(self):
        return f"{self.nombre}"
    class Meta:
        verbose_name = "Estado de la orden"
        verbose_name_plural = "Estados de la orden"