from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReservaSerializer, ReservaPorHabitacionSerializer

class ReservaView(APIView):
    def post(request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                                
class ReservaPorHabitacionView(APIView):
    def post(request):
        serializer = ReservaPorHabitacionSerializer(data=request.data)
        if serializer.is_valid():
            fechaIngreso = serializer.validated_data['fechaIngreso']
            fechaEgreso = serializer.validated_data['fechaEgreso']
            
            if fechaEgreso <= fechaIngreso:
                return Response({'error': 'Fecha de egreso debe ser posterior a la fecha de ingreso.'}, status=status.HTTP_400_BAD_REQUEST)

            if fechaIngreso < serializer.instance.reservaId.fechaReserva:
                return Response({'error': 'No se puede reservar una habitación para una fecha anterior a la fecha de reserva.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    