from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serializer import ClienteSerializer

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')  # PROCESA SOLICITUD Y RENDERIZA LA VISTA "login.html"

    def post(self, request):  # METODO POST QUE OBTIENE EL USUARIO Y CONTRASEÑA DE LOS DATOS ENVIADOS EN LA SOLICITUD.
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('admin:index')  # Redirigir al panel de control de Django para el superusuario
            else:
                return redirect('profile')  # Redirigir a la página de perfil para el usuario común
        else:
            messages.error(request, 'Credenciales inválidas')
            return redirect('login')

class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)
    
class SingupView(generics.CreateAPIView):
    serializer_class = ClienteSerializer