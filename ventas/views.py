from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny

class PagoViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Pago.
    """
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['fechahora_pago'] # Nuevo API filter

class OrdenViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Orden.
    """
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['fechahora_orden'] # Nuevo API filter

class DetalleOrdenViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de DetalleOrden.
    """
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['orden'] # Nuevo API filter
