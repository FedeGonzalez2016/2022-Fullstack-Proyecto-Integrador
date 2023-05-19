from django.db import models
from django.core.validators import RegexValidator

# Aquí se encuentra el código de las clases TipoHabitacion, Habitacion, Reserva y ReservaPorHabitacion

class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    usuario = models.EmailField(max_length=254, blank=False, unique=True)
    contraseña = models.CharField(max_length=150, blank=False)
    fechaDeNacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    class Meta:
        db_table = "Cliente"
        verbose_name = "Todos los clientes registrados"
        verbose_name_plural = "Clientes"
    def __unicode__(self):
        return self.correo
    def __str__(self) -> str:
        return f"Cliente {self.apellido}, {self.nombre}"
        
class Hotel(models.Model):
    hotelId = models.AutoField(primary_key=True)
    razonsocial= models.TextField(max_length=150, blank=False)
    cuil = models.TextField(blank=False, 
                            unique=True, 
                            validators=[RegexValidator(
                                regex="^(20|2[3-7]|30|3[3-4])(\d{8})(\d)$", 
                                message="CUIL inválido")])
    domicilio = models.TextField(max_length=150, blank=False)
    localidad = models.CharField(max_length=100,blank=False)
    provincia = models.CharField(max_length=100, blank=False)
    cp = models.PositiveSmallIntegerField(blank=False)
    telefono = models.IntegerField(blank=False)
    categoria = models.TextField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    class Meta:
        db_table = "Hotel"
        verbose_name = "Todos los hoteles disponibles"
        verbose_name_plural = "Hoteles"
    def __unicode__(self):
        return self.razonsocial
    def __str__(self) -> str:
        return self.razonsocial

class Empleado(models.Model):
    empleadoId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    usuario = models.EmailField(max_length=254, blank=False, unique=True)
    contraseña = models.CharField(max_length=150, blank=False)
    domicilio = models.TextField(max_length=150, blank=False)
    localidad = models.CharField(max_length=100, blank=False)
    provincia = models.CharField(max_length=100, blank=False)
    cp = models.PositiveSmallIntegerField(blank=False)
    telefono = models.IntegerField(blank=False)
    hotelId = models.ForeignKey(Hotel, to_field="hotelId", on_delete=models.CASCADE)
    rol = models.CharField(max_length=70, blank=False)
    class Meta:
        db_table = "Empleado"
        verbose_name = "Todos los empleados registrados en el hotel"
        verbose_name_plural = "Empleados"
    def __unicode__(self):
        return self.usuario
    def __str__(self) -> str:
        return f"Empleado {self.apellido}, {self.nombre}"