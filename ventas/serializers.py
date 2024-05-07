from rest_framework import serializers
from .models import *

class PagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class OrdenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

class DetalleOrdenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'
