from rest_framework import serializers
from .models import *

class TipoDocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class PaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class EstadoEntregaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EstadoEntrega
        fields = '__all__'

class EstadoOrdenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EstadoOrden
        fields = '__all__'
