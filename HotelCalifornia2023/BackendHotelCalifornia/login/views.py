#IMPORTACION DE LOS MODULOS NECESARIOS PARA EL FUNCIONAMIENTO DE LA APP

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

#Este archivo define las vistas, que son las funciones o clases que manejan las solicitudes HTTP entrantes y gcrean las respuestas.(Vistas de clases, de funciones o renderizado de plantillas.)

from django.contrib.auth import authenticate, login

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html') # PROCESA SOLICITUD Y RENDERIZA LA VISTA "login.html"

    def post(self, request): # METODO POST QUE OBTIENE EL USUARIO Y CONTRASEÑA DE LOS DATOS ENVIADOS EN LA SOLICITUD.
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password) # VERIFICA LAS CREDENCIALES DE USUARIO
        if user is not None: # SI todo ESTA BIEN, SE DEVUELVE RESPUESTA 200 INICIO DE SESION EXITOSO
            login(request, user)
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else: # SI LAS CREDENCIALES NO SON LAS CORRECTAS, SE ENVIA CODIGO 401 NO AUTORIZADO.
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
