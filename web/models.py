from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from configuracion.models import *

class UsuarioManager(BaseUserManager):
    def create_user(self, nombres, username, email, password = None):
        if not email:
            raise ValueError("El usuario debe registrar un correo electrónico")
        
        user = self.model(
            nombres = nombres,
            username = username,
            email = self.normalize_email(email),
            password = make_password(password, salt=None, hasher='default')
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nombres, username, email, password):
        user = self.create_user(
            nombres = nombres,
            username = username,
            email = email,
            password = password
        )
        user.usuario_administrador = True
        user.save()
        return user

class Usuario(AbstractBaseUser):
    username = models.CharField("Nombre de usuario", max_length = 100, unique = True)
    email = models.EmailField("Correo electrónico", max_length = 254, unique = True)
    nombres = models.CharField("Nombres", max_length = 200)
    apellido_p = models.CharField("Apellido paterno", max_length = 200, blank = True, null = True)
    apellido_m = models.CharField("Apellido materno", max_length = 200, blank = True, null = True)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete = models.CASCADE, verbose_name = "Tipo de documento", null = True, blank = True)
    numero_documento = models.CharField("Número de documento", max_length=100, null=True, blank=True)
    celular = models.CharField("Celular", max_length = 20, blank = True, null = True)
    #fecha_registro = models.DateTimeField(auto_now_add=True)
    
    usuario_administrador = models.BooleanField(default=False)
    usuario_activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombres"]
    
    def __str__(self):
        return f"{self.nombres} {self.apellido_p} {self.apellido_m}"

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
    
    @property
    def is_active(self):
        return self.usuario_activo

    @property
    def date_joined(self):
        return self.usuario_administrador

    def save(self, *args, **kwargs): # Hasheo de contraseñas
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        

"""
class PermissionManager(models.Manager):
   use_in_migrations = True
   def get_by_natural_key(self, codename, app_label, model):
        return self.get(
           codename = codename,
           content_type = ContentType.objects.db_manager(self.db).get_by_natural_key(
               app_label, model
           ),
        )
"""

"""
class Empleado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, verbose_name = "Usuario asociado")
    cargos = models.ManyToManyField(Group)
    #cargos = models.ManyToManyField(Cargo, through = 'AsignacionCargo')
    def __str__(self):
        return f"{self.usuario}"
        #return self.nombre
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
"""

