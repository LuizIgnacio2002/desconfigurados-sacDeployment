from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de TipoDocumento.
    """
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    #filterset_fields = ['nombre'] # Nuevo API filter
    filterset_fields = '__all__'

class PaisViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Pais.
    """
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [permissions.IsAuthenticated]
    #filterset_fields = ['nombre'] # Nuevo API filter
    filterset_fields = '__all__'

class CiudadViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Ciudad.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['nombre'] # Nuevo API filter

class EstadoEntregaViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de EstadoEntrega.
    """
    queryset = EstadoEntrega.objects.all()
    serializer_class = EstadoEntregaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['nombre'] # Nuevo API filter

class EstadoOrdenViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de EstadoOrden.
    """
    queryset = EstadoOrden.objects.all()
    serializer_class = EstadoOrdenSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['nombre'] # Nuevo API filter
