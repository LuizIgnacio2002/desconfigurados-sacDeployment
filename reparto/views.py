from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny

class UbicacionViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Ubicacion.
    """
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['ciudad'] # Nuevo API filter

class EntregaViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Entrega.
    """
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['fechahora_entrega'] # Nuevo API filter
