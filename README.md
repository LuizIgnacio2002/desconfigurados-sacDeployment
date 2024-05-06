# Backend del proyecto Ecommerce Smart Tachito

## Descripción del Proyecto Django

Este repositorio contiene el código fuente de un proyecto Django para un Ecommerce llamado Smart Tachito. El proyecto permite a los usuarios navegar por una tienda virtual, agregar productos al carrito de compras, realizar pedidos y gestionar sus cuentas.

## Tecnologías Utilizadas

- Django: Framework de desarrollo web Python para crear aplicaciones web dinámicas. (https://www.djangoproject.com/)
- djangorestframework: Framework de desarrollo RESTful para crear APIs con Django. (https://readthedocs.org/projects/django-rest-framework/)
- django-cors-headers: Middleware para permitir solicitudes CORS (Cross-Origin Resource Sharing) en aplicaciones Django. (https://pypi.org/project/django-cors-headers/)
- Pillow: Biblioteca para el procesamiento de imágenes en Python. (https://pillow.readthedocs.io/en/latest/installation.html)
- sqlparse: Biblioteca para analizar y manipular código SQL. (https://sqlparse.readthedocs.io/)
- asgiref: Library para la implementación de ASGI, el protocolo de comunicación entre servidores web y aplicaciones Python. (https://pypi.org/project/asgiref/)
- tzdata: Biblioteca para acceder a la información de zonas horarias. (https://docs.readthedocs.io/en/stable/config-file/v2.html)

## Versiones de las Tecnologías

- asgiref: 3.8.1
- Django: 5.0.4
- django-cors-headers: 4.3.1
- djangorestframework: 3.15.1
- Pillow: 10.3.0
- sqlparse: 0.5.0
- tzdata: 2024.1

## Instrucciones para instalación y ejecución

1. Cambiar al directorio del proyecto
```
python3 -m venv .venv
cd backend
```

2. Crear de un entorno virtual y activarlo
```
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias
```
pip install -r requirements.txt
```

4. Ejecutar el servidor de desarrollo
```
python manage.py runserver 0.0.0.0:8000
```

## Acceso a la aplicación

La aplicación estará disponible en http://localhost:8000. 

Además, se puede acceder a la administración de Django en http://localhost:8000/admin.