# Create your models here.
from django.db import models

class Remito(models.Model):
    # id = models.IntegerField(3)
    numero_remito = models.CharField(max_length=20)
    numero_viaje = models.IntegerField(5)
    detalle_transporte = models.CharField(max_length=30)
    deposito_id = models.ForeignKey('depositos.Deposito', on_delete=models.PROTECT)
    fecha_ingreso = models.DateTimeField
    usuario_id = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    aprobado = models.BooleanField(False)
    
    def __str__(self):
        return f"{self.numero_remito}"


class RemitoProducto(models.Model):
    # id = models.IntegerField(3)
    remito_id = models.ForeignKey('ingresos.Remito', on_delete=models.PROTECT)
    producto_id = models.ForeignKey('ingresos.Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField(4)
    actualizado = models.DateTimeField


class Producto(models.Model):
    # id = models.IntegerField(3)
    marca = models.CharField(30)
    modelo = models.CharField(50)

    def __str__(self):
        return f"{self.marca} {self.modelo}"