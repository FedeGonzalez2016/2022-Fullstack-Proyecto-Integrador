from rest_framework import  generics
from .serializer import ClienteSerializer

class SingupView(generics.CreateAPIView):
    serializer_class = ClienteSerializer
