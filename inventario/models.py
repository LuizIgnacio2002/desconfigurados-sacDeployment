from django.db import models

class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length = 100)
    descripcion = models.CharField("Descripción", max_length = 500)
    imagen = models.ImageField("Imagen", upload_to = "imagen/")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Categoria de productos"
        verbose_name_plural = "Categorias de productos"
        db_table = "Categoria"

class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length = 100)
    descripcion_breve = models.CharField("Descripción breve", max_length = 100)
    descripcion_extendida = models.CharField("Descripción extendida", max_length = 500)
    precio = models.DecimalField("Precio", max_digits=10 , decimal_places = 2)
    imagen_principal = models.ImageField("Imagen principal", upload_to = "imagen/")
    imagen_secundaria_1 = models.ImageField("Imagen secundaria 1", upload_to = "imagen/", blank = True, null = True)
    imagen_secundaria_2 = models.ImageField("Imagen secundaria 2", upload_to = "imagen/", blank = True, null = True)
    imagen_secundaria_3 = models.ImageField("Imagen secundaria 3", upload_to = "imagen/", blank = True, null = True)
    imagen_360 = models.ImageField("Imagen 360", upload_to = "imagen/", blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, verbose_name = "Categoría")
    stock = models.IntegerField("Stock", blank = True, null = True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "Producto"

class Residuo(models.Model):
    nombre = models.CharField("Nombre", max_length = 100)
    descripcion = models.CharField("Descripción", max_length = 500)
    imagen = models.ImageField("Imagen", upload_to = "imagen/")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Residuo"
        verbose_name_plural = "Residuos"
        db_table = "Residuo"

class Contenedor(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE, verbose_name = "Producto")
    residuo = models.ForeignKey(Residuo, on_delete = models.CASCADE, verbose_name = "Tipo de residuo que puede contener")
    def __str__(self):
        return f"{self.producto} {self.residuo}"
    class Meta:
        verbose_name = "Contenedor"
        verbose_name_plural = "Contenedores"
        db_table = "Contenedor"