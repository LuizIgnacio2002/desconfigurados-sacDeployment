from rest_framework import serializers
from .models import *

class UbicacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class EntregaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'
        #fields = ['ubicacion', 'empleado', 'fechahora_entrega', 'detalles_entrega', 'estado_entrega']
