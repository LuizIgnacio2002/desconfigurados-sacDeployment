from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Usuario.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    #filterset_fields = ['username'] # Nuevo API filter
    #lookup_field = 'username'

class GroupViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    #lookup_field = 'name'