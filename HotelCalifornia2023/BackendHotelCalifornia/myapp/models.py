from django.db import models

class Hotel(models.Model):
    Hotel_Id = models.AutoField(primary_key=True)
    Hotel_RazonSocial = models.CharField(max_length=50)
    Hotel_Cuil = models.IntegerField()
    Hotel_Domicilio = models.CharField(max_length=50)
    Hotel_Localidad = models.CharField(max_length=50)
    Hotel_Provincia = models.CharField(max_length=50)
    Hotel_CP = models.IntegerField()
    Hotel_Telefono = models.IntegerField()
    Hotel_Categoria = models.CharField(max_length=50)
    Hotel_Email = models.CharField(max_length=50)

class Empleado(models.Model):
    Empleadoid = models.AutoField(primary_key=True)
    Empleado_Nombre = models.CharField(max_length=50)
    Empleado_Apellido = models.CharField(max_length=50)
    Empleado_Usuario = models.CharField(max_length=50)
    Empleado_Correo = models.CharField(max_length=50)
    Empleado_Password = models.CharField(max_length=50)
    Empleado_Domicilio = models.CharField(max_length=50)
    Empleado_Localidad = models.CharField(max_length=50)
    Empleado_Provincia = models.CharField(max_length=50)
    Empleado_CP = models.IntegerField()
    Empleado_Telefono = models.IntegerField()
    Empleado_Rol = models.CharField(max_length=50)
    Hotel_Id = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Tipo(models.Model):
    Tipo_Id = models.AutoField(primary_key=True)
    Tipo_Descripcion = models.CharField(max_length=50)

class Habitacion(models.Model):
    Habitacion_Id = models.AutoField(primary_key=True)
    Habitacion_Numero = models.IntegerField()
    Habitacion_Piso = models.IntegerField()
    Habitacion_Estado = models.CharField(max_length=50)
    Habitacion_Precio = models.IntegerField()
    Hotel_Id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Tipo_Id = models.ForeignKey(Tipo, on_delete=models.CASCADE)

class Factura(models.Model):
    Factura_Id = models.AutoField(primary_key=True)
    Factura_Numero = models.IntegerField()
    Hotel_Id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Cliente_Id = models.ForeignKey('Cliente', on_delete=models.CASCADE)

class Cliente(models.Model):
    Cliente_Id = models.AutoField(primary_key=True)
    Cliente_Nombre = models.CharField(max_length=50)
    Cliente_Apellido = models.CharField(max_length=50)
    Cliente_Correo = models.CharField(max_length=50)
    Cliente_Password = models.CharField(max_length=50)
    Cliente_Nacimiento = models.DateField()

class Reserva(models.Model):
    Reserva_Id = models.AutoField(primary_key=True)
    Fecha_Reserva = models.DateField()
    Cliente_Id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Detalle(models.Model):
    Detalle_Id = models.AutoField(primary_key=True)
    Detalle_Descuento = models.CharField(max_length=50)
    Detalle_Importe = models.IntegerField()
    Factura_Id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    Reserva_Id = models.ForeignKey(Reserva, on_delete=models.CASCADE)

class Reserva_Habitacion(models.Model):
    Reserva_Habitacion_Id = models.AutoField(primary_key=True)
    Fecha_Ingreso = models.DateField()
    Fecha_Egreso = models.DateField()
    Habitacion_Id = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    Reserva_Id = models.ForeignKey(Reserva, on_delete=models.CASCADE)

class Tipo_Pago(models.Model):
    Tipo_Pago_Id = models.AutoField(primary_key=True)
    Tipo = models.CharField(max_length=50)

class Detalle_Pago(models.Model):
    Detalle_Pago_Id = models.AutoField(primary_key=True)
    Porcentaje_Pago = models.CharField(max_length=50)
    Factura_Id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    Tipo_Pago_Id = models.ForeignKey(Tipo_Pago, on_delete=models.CASCADE)