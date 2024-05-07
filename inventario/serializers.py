from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ResiduoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Residuo
        fields = '__all__'

class ContenedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contenedor
        fields = '__all__'
