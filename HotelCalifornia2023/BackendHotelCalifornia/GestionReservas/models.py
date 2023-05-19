from django.db import models
from GestionUsuarios.models import Hotel, Cliente

# Aquí se encuentra el código de las clases Tipo, Habitacion, Reserva y ReservaHabitacion


class Tipo(models.Model):
    tipoId = models.AutoField(primary_key=True)
    tipoDescripcion = models.CharField(max_length=50)

    class Meta:
        db_table = "tipo"
        verbose_name = "Tipos de habitaciones de un hotel"
        verbose_name_plural = "tipos"
        def __unicode__(self):
            return "tipo"
        def __str__(self):
            return self.tipo_habitacion

class Habitacion(models.Model):
    habitacionId = models.AutoField(primary_key=True)
    habitacionNumero = models.IntegerField()
    habitacionPiso = models.IntegerField()
    habitacionEstado = models.CharField(max_length=50)
    habitacionPrecio = models.IntegerField()
    hotelId = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    tipoId = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        db_table = "habitacion"
        verbose_name = "Habitaciones de un hotel"
        verbose_name_plural = "habitaciones"
        def __unicode__(self):
            return "habitacion"
        def __str__(self):
            return self.habitacion

class Reserva(models.Model):
    reservaId = models.AutoField(primary_key=True)
    fechaReserva = models.DateField()
    clienteId = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    class Meta:
        db_table = "reserva"
        verbose_name = "Reservas de un hotel"
        verbose_name_plural = "reservas"
        def __unicode__(self):
            return "reserva"
        def __str__(self):
            return self.reserva

class ReservaHabitacion(models.Model):
    reservaHabitacionId = models.AutoField(primary_key=True)
    fechaIngreso = models.DateField()
    fechaEgreso = models.DateField()
    habitacionId = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    reservaId = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    class Meta:
        db_table = "reserva_habitacion"
        verbose_name = "Habitaciones en una reserva"
        verbose_name_plural = "reserva_habitaciones"
        def __unicode__(self):
            return "reserva_habitacion"
        def __str__(self):
            return self.reserva_habitacion
