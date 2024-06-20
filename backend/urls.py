"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from configuracion import views as views_configuracion
from inventario import views as views_inventario
from reparto import views as views_reparto
from ventas import views as views_ventas
from web import views as views_web

admin.site.site_header = 'Ecommerce Smart Tachito'
admin.site.site_title = "Ecommerce Smart Tachito"
admin.site.index_title = "Panel de Control"

router = routers.DefaultRouter()
# Configuracion
router.register(r'tiposdocumento', views_configuracion.TipoDocumentoViewSet)
router.register(r'paises', views_configuracion.PaisViewSet)
router.register(r'ciudades', views_configuracion.CiudadViewSet)
router.register(r'estadosentrega', views_configuracion.EstadoEntregaViewSet)
router.register(r'estadosorden', views_configuracion.EstadoOrdenViewSet)
# Inventario
router.register(r'categorias', views_inventario.CategoriaViewSet)
router.register(r'productos', views_inventario.ProductoViewSet)
router.register(r'residuos', views_inventario.ResiduoViewSet)
router.register(r'contenedores', views_inventario.ContenedorViewSet)
# Reparto
router.register(r'ubicaciones', views_reparto.UbicacionViewSet)
router.register(r'entregas', views_reparto.EntregaViewSet)
# Ventas
router.register(r'pagos', views_ventas.PagoViewSet)
router.register(r'ordenes', views_ventas.OrdenViewSet)
router.register(r'detallesorden', views_ventas.DetalleOrdenViewSet)
# Web
router.register(r'usuarios', views_web.UsuarioViewSet)
router.register(r'roles', views_web.GroupViewSet)

#router.register(r'usertypes', views.UserTypeViewSet)
#router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin", admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)