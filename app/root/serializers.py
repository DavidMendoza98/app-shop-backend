from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
   # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','user_permissions']

class GroupSerializer(serializers.ModelSerializer):
   # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = Group
        fields = '__all__'

class TipoTiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTienda
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'

class EstadoCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCredito
        fields = '__all__'

class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields = '__all__'

class TiendaSerializer(serializers.ModelSerializer):
    #tipo_tienda = TipoTiendaSerializer(depth=1)
    class Meta:
        model = Tienda
        fields = '__all__'
        #exclude = ['isDelete','created_at']

class TiendaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        exclude = ['isDelete','created_at']
        depth = 1

class ProductoSerializer(serializers.ModelSerializer):
    #tipo_tienda = TipoTiendaSerializer(depth=1)
    class Meta:
        model = Producto
        fields = '__all__'
        #exclude = ['isDelete','created_at']

class ProductoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude = ['isDelete','created_at']
        depth = 1

class LoteSerializer(serializers.ModelSerializer):
    #tipo_tienda = TipoTiendaSerializer(depth=1)
    class Meta:
        model = Lote
        fields = '__all__'
        #exclude = ['isDelete','created_at']

class LoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        exclude = ['isDelete','created_at']
        depth = 1

class PedidoSerializer(serializers.ModelSerializer):
    #tipo_tienda = TipoTiendaSerializer(depth=1)
    class Meta:
        model = Pedido
        fields = '__all__'
        #exclude = ['isDelete','created_at']

class PedidoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        exclude = ['isDelete','created_at']
        depth = 1

class DetallePedidoSerializer(serializers.ModelSerializer):
    #tipo_tienda = TipoTiendaSerializer(depth=1)
    class Meta:
        model = DetallePedido
        fields = '__all__'
        #exclude = ['isDelete','created_at']

class DetallePedidoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        exclude = ['isDelete','created_at']
        depth = 1

class CreditoSerializer(serializers.ModelSerializer):
    #tipo_tienda = TipoTiendaSerializer(depth=1)
    class Meta:
        model = Credito
        fields = '__all__'
        #exclude = ['isDelete','created_at']

class CreditoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        exclude = ['isDelete','created_at']
        depth = 1

class VentaSerializer(serializers.ModelSerializer):
    #tipo_tienda = TipoTiendaSerializer(depth=1)
    class Meta:
        model = Venta
        fields = '__all__'
        #exclude = ['isDelete','created_at']

class VentaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        exclude = ['isDelete','created_at']
        depth = 1
