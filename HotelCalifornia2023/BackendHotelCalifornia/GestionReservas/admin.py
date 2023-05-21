from django.contrib import admin
from .models import TipoHabitacion, Habitacion, Reserva, ReservaPorHabitacion

class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ["tipoHabitacion"]
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ("numero", "piso", "estado", "precio", "hotelId", "tipoHabitacionId")
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("fechaReserva", "clienteId")
class ReservaPorHabitacionAdmin(admin.ModelAdmin):
    list_display = ("fechaIngreso", "fechaEgreso", "habitacionId", "reservaId")

admin.site.register(TipoHabitacion, TipoHabitacionAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(ReservaPorHabitacion, ReservaPorHabitacionAdmin)