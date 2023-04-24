from rest_framework import routers
from .api import * # importa todos los viewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet,'user')
router.register('shop', TiendaViewSet,'Tienda')
router.register('shop_type', TipoTiendaViewSet,'TipoTienda')
router.register('category', CategoriaViewSet,'Categoria')
router.register('product', ProductoViewSet,'Producto')
router.register('lot', LoteViewSet,'Lote')
router.register('order_status', EstadoPedidoViewSet,'EstadoPedido')
router.register('order', PedidoViewSet,'Pedido')
router.register('order_detail', DetallePedidoViewSet,'DetallePedido')
router.register('payment_type', TipoPagoViewSet,'TipoPago')
router.register('credit_status', EstadoCreditoViewSet,'EstadoCredito')
router.register('credit', CreditoViewSet,'Credito')
router.register('sales', VentaViewSet,'Venta')


#router.register('')
urlpatterns = router.urls


