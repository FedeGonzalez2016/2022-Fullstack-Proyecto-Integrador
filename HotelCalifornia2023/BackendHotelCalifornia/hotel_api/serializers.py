from rest_framework import serializers
from GestionReservas.models import Reserva, ReservaPorHabitacion

class ReservaSerializer(serializers.ModelSerializer):
    fechaReserva=serializers.DateField(required = False),
    clienteId=serializers.IntegerField(required = True)
    class Meta:
        model = Reserva
        fields = '__all__'

class ReservaPorHabitacionSerializer(serializers.ModelSerializer):
    fechaIngreso=serializers.CharField(required = True),
    fechaEgreso=serializers.CharField(required = True),
    habitacionId=serializers.EmailField(required = True),
    reservaId=serializers.DateField(required = True),
    class Meta:
        model = ReservaPorHabitacion
        fields = '__all__'