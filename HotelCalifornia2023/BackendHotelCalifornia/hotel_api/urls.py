from django.urls import path
from .views import ReservaView, ReservaPorHabitacionView

urlpatterns = [
    path('reserva/crear', ReservaView.as_view(), name='crear_reserva'),
    path('reservaHabitacion/crear', ReservaPorHabitacionView.as_view(), name='crear_reserva_por_habitacion'),
]
