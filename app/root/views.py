from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from root.models import *
from .serializers import UserSerializer
# Create your views here.


class LoginV2(APIView):
    #permission_classes = [AllowAny]
    def post(self, request):
        # Obtener los datos de la petición
        username = request.data.get("username")
        password = request.data.get("password")

        # Autenticar al usuario
        user = authenticate(username=username, password=password)
        if(not user):
            return Response(
                {"error": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        login(request,user)
        if user is None:
            return Response(
                {"error": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Obtener el token de autenticación
        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user) 
        return Response(
            {
                "token": token.key,
                "user":  serializer.data
            },
            status=status.HTTP_200_OK
        )

class logout(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        try:
            token = request.auth
            token.delete()
            logout(request)
            return Response(status.HTTP_200_OK)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

