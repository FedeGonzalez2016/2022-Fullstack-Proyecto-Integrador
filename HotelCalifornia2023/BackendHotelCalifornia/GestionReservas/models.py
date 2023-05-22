from django.db import models
from django.db.models import Q
from django.db.models.functions import Now
from datetime import date
from GestionUsuarios.models import Hotel, Cliente

# Aquí se encuentra el código de las clases TipoHabitacion, Habitacion, Reserva y ReservaPorHabitacion

class TipoHabitacion(models.Model):
    tipoHabitacionId = models.AutoField(primary_key=True)
    tipoHabitacion = models.CharField(max_length=50, unique=True, blank=False)
    class Meta:
        db_table = "tipo"
        verbose_name = "Tipos de habitaciones de un hotel"
        verbose_name_plural = "Tipos"
    def __unicode__(self):
        return self.tipoHabitacion
    def __str__(self) -> str:
        return self.tipoHabitacion

class Habitacion(models.Model):
    habitacionId = models.AutoField(primary_key=True)
    numero = models.PositiveSmallIntegerField(blank=False, unique=True)
    piso = models.PositiveSmallIntegerField(blank=False)
    estado = models.CharField(max_length=50, default="Disponible", blank=False)
    precio = models.IntegerField(blank=False)
    hotelId = models.ForeignKey(Hotel, to_field='hotelId', on_delete=models.CASCADE)
    tipoHabitacionId = models.ForeignKey(TipoHabitacion, to_field="tipoHabitacionId", on_delete=models.CASCADE)
    class Meta:
        db_table = "habitacion"
        verbose_name = "Habitaciones de un hotel"
        verbose_name_plural = "Habitaciones"
    def __unicode__(self):
        return f"Habitacion {self.numero}"
    def __str__(self) -> str:
        return f"Habitacion {self.numero}"

class Reserva(models.Model):
    reservaId = models.AutoField(primary_key=True)
    fechaReserva = models.DateField(default=date.today, blank=False)
    clienteId = models.ForeignKey(Cliente, to_field='clienteId', on_delete=models.CASCADE)
    class Meta:
        db_table = "reserva"
        verbose_name = "Reservas de habitacinoes en un hotel"
        verbose_name_plural = "Reservas"
    def __unicode__(self):
        return f"Reserva {self.reservaId}"
    def __str__(self):
        return f"Reserva del cliente {self.clienteId} el {self.fechaReserva}"

class ReservaPorHabitacion(models.Model):
    reservaHabitacionId = models.AutoField(primary_key=True)
    fechaIngreso = models.DateField(blank=False)
    fechaEgreso = models.DateField(blank=False)
    habitacionId = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    reservaId = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    class Meta:
        db_table = "reserva_habitacion"
        verbose_name = "Habitaciones en una reserva"
        verbose_name_plural = "reserva_habitaciones"
        constraints = [
            models.CheckConstraint(
                check=models.Q(fechaIngreso__lte=models.F('fechaEgreso'), fechaIngreso__gte=Now()),
                name='Correctas fecha de reserva'
            ),
        ]
    def __unicode__(self):
        return self.reservaHabitacionId
    def __str__(self) -> str:
        return f"Reserva {self.reservaId}, fecha ingreso {self.fechaEgreso}, fecha egreso {self.fechaEgreso}, habitacion {self.habitacionId}"
