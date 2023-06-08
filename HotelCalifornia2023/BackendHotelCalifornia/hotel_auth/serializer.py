from rest_framework import serializers
from GestionUsuarios.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    nombre=serializers.CharField(required = True),
    apellido=serializers.CharField(required = True),
    usuario=serializers.EmailField(required = True),
    password=serializers.CharField(required = True),
    fechaDeNacimiento=serializers.DateField(required = True),
    class Meta:
        model = Cliente
        fields = '__all__'
