from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class registroCodigoAuth(models.Model):
    codigo = models.CharField(max_length=6)
    fecha = models.DateTimeField()
    isComfirm = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()

    def __str__(self):
        return "{} {} {}".format(self.codigo, self.user, self.fecha)

class Logs(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo_evento = models.CharField( max_length=30)
    tabla_afectada = models.CharField( max_length=30)
    descripcion = models.TextField()
    origen = models.CharField( max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {}".format(self.user, self.tipo_evento, self.tabla_afectada,self.fecha_hora)

class TipoTienda(models.Model):
    tipoTienda = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return self.tipoTienda

class Tienda(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.TextField()
    telefonoFijo = models.CharField( max_length=15)
    whatsapp = models.CharField( max_length=15)
    e_mail = models.CharField(max_length=50)
    web_site = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    idTipoTienda = models.ForeignKey(TipoTienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class User_Tienda(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()

    def __str__(self):
        return "{} {}".format(self.user, self.tienda)

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return self.categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=20)
    img_link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    isPublic = models.BooleanField()
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
class Lote(models.Model):
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {} {}".format(self.producto, self.precio, self.fecha_vencimiento)

class TipoPago(models.Model):
    tipoPago = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return self.tipoPago

class EstadoPedido(models.Model):
    estadoPedido = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return self.estadoPedido

class Pedido(models.Model):
    fecha = models.DateTimeField( auto_now=False, auto_now_add=False)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    estado_pedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return "{} {} {}".format(self.user, self.tienda, self.fecha)

class DetallePedido(models.Model):
    cantidad = models.IntegerField()
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return "{} {} {}".format(self.cantidad, self.lote, self.pedido)

class EstadoCredito(models.Model):
    estadoCredito = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return self.estadoCredito

class Credito(models.Model):
    monto = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_credito = models.DateTimeField()
    plazo_dias = models.IntegerField()
    estado = models.ForeignKey(EstadoCredito, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return "{} {} {} {}".format(self.user, self.monto, self.pedido, self.estado)

class Venta(models.Model):
    monto_vendido = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_venta = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return "{} {} {} {}".format(self.user,self.pedido, self.monto_vendido, self.fecha_venta)
