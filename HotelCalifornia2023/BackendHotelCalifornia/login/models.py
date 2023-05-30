# IMPORTACION DE MODULOS NECESARIOS PARA EL FUNCIONAMIENTO CORRECTO DE LA APLICACION
# ARCHIVO QUE DEFINE LOS modelos de base de datos que representan las entidades y estructura de datos de tu aplicación.  CADA MODELO EN DJANGO ->> TABLA EN BD .// define los campos y relaciones de esa tabla.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class CustomUserManager(BaseUserManager): # DEFINE CLASE CUSTOMUSERMANAGER QUE HEREDA DE BASEUSERMANAGER
    def create_user(self, email, password=None, **extra_fields): # CREA USUARIO - VERIFICA QUE HAY CORREO ELECTRONICO.
        if not email:
            raise ValueError('El campo "email" es obligatorio')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields) # CREA USUARIO UTILIZANDO MODELO CUSTOM USER.
        user.set_password(password) # ESTABLECEMOS CONTRASEÑA
        user.save(using=self._db) # SE ALMACENA EN LA BASE DE DATOS
        return user # DEVOLVEMOS USUARIO.

        # CREA SUPER USUARIO.
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) # OTORGA PERMISOS DE ADMINISTRADOR
        extra_fields.setdefault('is_superuser', True) # OTORGA PERMISOS DE ADMINISTRADOR
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Email') # CAMPO EMAIL UNICO
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # NO PERTENECE AL STAFF NI ES ADMIN

    # SIN COMENTARIOS 
    groups = models.ManyToManyField(
        Group,
        verbose_name='Groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
    # SIN COMENTARIOS
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='User permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' #  Especifica el campo email como el campo de nombre de usuario utilizado para la autenticación.

    def __str__(self):
        return self.email
