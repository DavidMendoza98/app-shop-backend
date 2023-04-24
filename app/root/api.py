from .models import *
from rest_framework import viewsets,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions,DjangoObjectPermissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes=[TokenAuthentication]
    

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()
        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = self.serializer_class(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "auth.view_user" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "auth.add_user" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        user = super().create(request, *args, **kwargs)
        #user.groups.add(grupo_cliente)  # Agrega el usuario al grupo "cliente"
        #user.save()
        print(user)
        return Response(status.HTTP_200_OK)
    
    def perform_create(self, serializer):
        user = serializer.save()  # Guarda la instancia del usuario creado
        grupo_cliente = Group.objects.get(name='cliente')
        user.groups.add(grupo_cliente)  # Agrega el usuario al grupo "cliente"
        user.save()  # Guarda el usuario actualizado

        # Ahora, la variable `user` contiene la instancia del usuario recién creado con el grupo "cliente" agregado.
        # Puedes hacer cualquier otra cosa que necesites con esta instancia, como devolverla en la respuesta HTTP.
        return user


class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all().filter(isDelete=False)
    serializer_class = TiendaSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = TiendaListSerializer(queryset, many=True)
        print(permisos)
        # Devolver la respuesta adecuada
        if(not "root.view_tienda" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TiendaListSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_tienda" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.add_tienda" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.change_tienda" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.delete_tienda" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Obtenga el objeto que se va a eliminar utilizando el ID de la URL
        instance = self.get_object()

        # Actualice el campo isDelete en el objeto y guárdelo en la base de datos
        instance.isDelete = True
        instance.save()

        # Devuelva una respuesta adecuada
        return Response(status=status.HTTP_204_NO_CONTENT)

class TipoTiendaViewSet(viewsets.ModelViewSet):
    queryset = TipoTienda.objects.all().filter(isDelete=False)
    serializer_class = TipoTiendaSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = TipoTiendaSerializer(queryset, many=True)
        print(permisos)
        # Devolver la respuesta adecuada
        if(not "root.view_tipotienda" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TipoTiendaSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_tipotienda" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().filter(isDelete=False)
    serializer_class = CategoriaSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = CategoriaSerializer(queryset, many=True)
        print(permisos)
        # Devolver la respuesta adecuada
        if(not "root.view_categoria" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategoriaSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_categoria" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().filter(isDelete=False)
    serializer_class = ProductoSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = ProductoListSerializer(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "root.view_producto" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductoListSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_producto" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.add_producto" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.change_producto" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.delete_producto" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Obtenga el objeto que se va a eliminar utilizando el ID de la URL
        instance = self.get_object()

        # Actualice el campo isDelete en el objeto y guárdelo en la base de datos
        instance.isDelete = True
        instance.save()

        # Devuelva una respuesta adecuada
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all().filter(isDelete=False)
    serializer_class = LoteSerializer
    #authentication_classes=[TokenAuthentication] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = LoteListSerializer(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "root.view_lote" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductoListSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_lote" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.add_lote" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.change_lote" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.delete_lote" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Obtenga el objeto que se va a eliminar utilizando el ID de la URL
        instance = self.get_object()

        # Actualice el campo isDelete en el objeto y guárdelo en la base de datos
        instance.isDelete = True
        instance.save()

        # Devuelva una respuesta adecuada
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstadoPedidoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all().filter(isDelete=False)
    serializer_class = EstadoPedidoSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = EstadoPedidoSerializer(queryset, many=True)
        print(permisos)
        # Devolver la respuesta adecuada
        if(not "root.view_estadopedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EstadoPedidoSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_estadopedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)

class TipoPagoViewSet(viewsets.ModelViewSet):
    queryset = TipoPago.objects.all().filter(isDelete=False)
    serializer_class = TipoPagoSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = TipoPagoSerializer(queryset, many=True)
        print(permisos)
        # Devolver la respuesta adecuada
        if(not "root.view_tipopago" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TipoPagoSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_tipopago" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().filter(isDelete=False)
    serializer_class = PedidoSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = PedidoListSerializer(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "root.view_pedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PedidoListSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_pedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.add_pedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.change_pedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.delete_pedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Obtenga el objeto que se va a eliminar utilizando el ID de la URL
        instance = self.get_object()

        # Actualice el campo isDelete en el objeto y guárdelo en la base de datos
        instance.isDelete = True
        instance.save()

        # Devuelva una respuesta adecuada
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all().filter(isDelete=False)
    serializer_class = DetallePedidoSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = DetallePedidoListSerializer(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "root.view_detallepedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DetallePedidoListSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_detallepedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.add_detallepedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.change_detallepedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.delete_detallepedido" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Obtenga el objeto que se va a eliminar utilizando el ID de la URL
        instance = self.get_object()

        # Actualice el campo isDelete en el objeto y guárdelo en la base de datos
        instance.isDelete = True
        instance.save()

        # Devuelva una respuesta adecuada
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstadoCreditoViewSet(viewsets.ModelViewSet):
    queryset = EstadoCredito.objects.all().filter(isDelete=False)
    serializer_class = EstadoCreditoSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = EstadoCreditoSerializer(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "root.view_estadocredito" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EstadoCreditoSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_estadocredito" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)

class CreditoViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all().filter(isDelete=False)
    serializer_class = CreditoSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = CreditoListSerializer(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "root.view_credito" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CreditoListSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_credito" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.add_credito" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.change_credito" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.delete_credito" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Obtenga el objeto que se va a eliminar utilizando el ID de la URL
        instance = self.get_object()

        # Actualice el campo isDelete en el objeto y guárdelo en la base de datos
        instance.isDelete = True
        instance.save()

        # Devuelva una respuesta adecuada
        return Response(status=status.HTTP_204_NO_CONTENT)

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all().filter(isDelete=False)
    serializer_class = VentaSerializer
    authentication_classes=[TokenAuthentication] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # Obtener todos los objetos de la base de datos
        queryset = self.get_queryset()
        permisos = request.user.get_all_permissions()

        # Incluir los datos de las llaves foráneas en el serializer utilizando el parámetro 'depth'
        serializer = VentaListSerializer(queryset, many=True)
        # Devolver la respuesta adecuada
        if(not "root.view_venta" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = VentaListSerializer(instance)

        permisos = request.user.get_all_permissions()
        if(not "root.view_venta" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.add_venta" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.change_venta" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permisos = request.user.get_all_permissions()
        if(not "root.delete_venta" in permisos):
            return Response(
                {"error": "No cuenta con los permisos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Obtenga el objeto que se va a eliminar utilizando el ID de la URL
        instance = self.get_object()

        # Actualice el campo isDelete en el objeto y guárdelo en la base de datos
        instance.isDelete = True
        instance.save()

        # Devuelva una respuesta adecuada
        return Response(status=status.HTTP_204_NO_CONTENT)
