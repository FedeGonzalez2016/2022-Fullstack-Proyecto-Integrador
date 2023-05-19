from django.db import models

class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    correo = models.CharField(max_length=100, blank=False)
    contraseña = models.CharField(max_length=150, blank=False)
    fechadenacimiento = models.DateField(blank=False)
    class Meta:
        db_table = "Cliente"
        verbose_name = "Todos los clientes registrados en el Hotel"
        verbose_name_plural = "Clientes"
        def __unicode__(self):
            return "Cliente"
        def __str__(self):
            return self.nombre
        
class Hotel(models.Model):
    hotelId = models.AutoField(primary_key=True)
    razonsocial= models.CharField(max_length=100, blank=False)
    cuil = models.IntegerField(blank=False)
    domicilio = models.TextField(max_length=100, blank=False)
    localidad = models.CharField(max_length=100,blank=False)
    provincia = models.CharField(max_length=100, blank=False)
    cp = models.IntegerField(blank=False)
    telefono = models.IntegerField(max_length=20, blank=False)
    categoria = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=80, blank=False)
    class Meta:
        db_table = "Hotel"
        verbose_name = "Todos los hoteles disponibles"
        verbose_name_plural = "Hoteles"
        def __unicode__(self):
            return "Hotel"
        def __str__(self):
            return self.razonsocial

class Empleado(models.Model):
    empleadoId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    usuario = models.CharField(max_length=50, blank=False)
    correo = models.CharField(max_length=100, blank=False)
    contraseña = models.CharField(max_length=100, blank=False)
    domicilio = models.CharField(max_length=100, blank=False)
    localidad = models.CharField(max_length=100, blank=False)
    provincia = models.CharField(max_length=100, blank=False)
    cp = models.IntegerField(blank=False)
    telefono = models.IntegerField(blank=False)
    hotelId = models.ForeignKey(Hotel, to_field="hotelId", on_delete=models.CASCADE)
    rol = models.CharField(max_length=70 ,blank=False)
    class Meta:
        db_table = "Empleado"
        verbose_name = "Todos los empleados registrados en el hotel"
        verbose_name_plural = "Empleados"
        def __unicode__(self):
            return "Empleado"
        def __str__(self):
            return self.nombre