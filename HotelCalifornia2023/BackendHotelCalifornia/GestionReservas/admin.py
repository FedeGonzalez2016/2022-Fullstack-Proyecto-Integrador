from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import TipoHabitacion, Habitacion, Reserva, ReservaPorHabitacion, Imagen

class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ["tipoHabitacion"]

class HabitacionAdminForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'
        widgets = {
            'imagenes': FilteredSelectMultiple('Imágenes', False),
        }
class HabitacionAdmin(admin.ModelAdmin):
    form = HabitacionAdminForm
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("fechaReserva", "clienteId")
class ReservaPorHabitacionAdmin(admin.ModelAdmin):
    list_display = ("fechaIngreso", "fechaEgreso", "habitacionId", "reservaId")

class ImagenAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoHabitacion, TipoHabitacionAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(ReservaPorHabitacion, ReservaPorHabitacionAdmin)