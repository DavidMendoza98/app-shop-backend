from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session

# Register your models here.
@admin.register(Tienda)
class Tienda_Admin(admin.ModelAdmin):
    pass

@admin.register(TipoTienda)
class TipoTienda_Admin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class Categoria_Admin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class Producto_Admin(admin.ModelAdmin):
    pass

@admin.register(Lote)
class Lote_Admin(admin.ModelAdmin):
    pass

@admin.register(EstadoPedido)
class EstadoPedido_Admin(admin.ModelAdmin):
    pass

@admin.register(TipoPago)
class TipoPago_Admin(admin.ModelAdmin):
    pass

@admin.register(Pedido)
class Pedido_Admin(admin.ModelAdmin):
    pass

@admin.register(DetallePedido)
class DetallePedido_Admin(admin.ModelAdmin):
    pass
    
@admin.register(EstadoCredito)
class DetallePedido_Admin(admin.ModelAdmin):
    pass

@admin.register(Credito)
class DetallePedido_Admin(admin.ModelAdmin):
    pass


@admin.register(Venta)
class Venta_Admin(admin.ModelAdmin):
    pass