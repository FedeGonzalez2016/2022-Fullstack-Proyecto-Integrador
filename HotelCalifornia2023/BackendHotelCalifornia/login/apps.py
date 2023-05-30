from django.apps import AppConfig

#Archivo necesario  solo si deseas ajustar o personalizar la configuración de tu aplicación (Nombre de la aplicacion, Permisos y Señales, etc)

class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'
