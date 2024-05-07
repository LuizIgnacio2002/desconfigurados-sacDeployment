from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Universities to be viewed or edited.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]  # Cambiamos IsAuthenticated por AllowAny
    filterset_fields = ['nombre'] # Nuevo API filter

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Universities to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]  # Cambiamos IsAuthenticated por AllowAny
    filterset_fields = ['nombre'] # Nuevo API filter

class ResiduoViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Residuo.
    """
    queryset = Residuo.objects.all()
    serializer_class = ResiduoSerializer
    permission_classes = [AllowAny]  # Cambiamos IsAuthenticated por AllowAny
    filterset_fields = ['nombre'] # Nuevo API filter

class ContenedorViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Contenedor.
    """
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorSerializer
    permission_classes = [AllowAny]  # Cambiamos IsAuthenticated por AllowAny
    filterset_fields = ['producto'] # Nuevo API filter
