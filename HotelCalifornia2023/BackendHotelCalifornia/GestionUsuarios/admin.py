from django.contrib import admin
from .models import Cliente, Hotel, Empleado

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "usuario", "contraseña", "fechaDeNacimiento")
class HotelAdmin(admin.ModelAdmin):
    list_display = ("razonsocial", "cuil", "domicilio", "localidad", "provincia", "cp", "telefono", "categoria", "email")
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "usuario", "contraseña", "domicilio", "localidad", "provincia", "cp", "telefono", "hotelId", "rol")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Empleado, EmpleadoAdmin)