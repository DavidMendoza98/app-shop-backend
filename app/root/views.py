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
from .serializers import UserSerializer,LoteListSerializer, ProductoListSerializer
# Create your views here.
class lotByProduct(APIView):
    #permission_classes = [AllowAny]
    def get(self, request):
        productId = request.query_params.get("id")
        product = Producto.objects.get(id = productId)
        lots = Lote.objects.all().filter(producto=product)
        data = LoteListSerializer(lots, many=True)
        return Response({'data':data.data})
        # try:
        #     lots = Lote.objects.all().filter(isDelete=False,producto=product)
        #     return Response({LoteListSerializer(lots)})
        # except:
        #     return Response({'message':'error'})

class productByCodigo(APIView):
    #permission_classes = [AllowAny]
    def get(self, request):
        productId = request.query_params.get("id")
        product = Producto.objects.filter(codigo = productId)
        #lotes = Lote.objects.all().filter(isDelete=False, producto = product)
        #data2 = LoteListSerializer(lotes, many=True)
        data = ProductoListSerializer(product, many=True)
        return Response({'data':data.data})


class home(APIView):
    def get(self,request):
        return Response(
            {
                "message":"Welcome"
            }
        )



class Login(APIView):
    #permission_classes = [AllowAny]
    def get(self, request):
        
        # Obtener los datos de la petición
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        # return Response({
        #     'usuario':username,
        #     'contra':password
        # })
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
    def post(self,request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response(status.HTTP_200_OK)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

class check(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        try:
            token = request.user.auth_token
            print(token)
            return Response(status.HTTP_200_OK)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
