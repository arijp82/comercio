# Create your models here.
from django.db import models

class Remito(models.Model):
    id = models.AutoField(primary_key=True)
    numero_remito = models.CharField(max_length=20)
    numero_viaje = models.IntegerField()
    detalle_transporte = models.CharField(max_length=30)
    deposito_id = models.ForeignKey('depositos.Deposito', on_delete=models.PROTECT)
    fecha_ingreso = models.DateTimeField()
    usuario_id = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    aprobado = models.BooleanField(False)
    
    def __str__(self):
        return f"{self.numero_remito}"


class RemitoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    remito_id = models.ForeignKey('Remito', on_delete=models.PROTECT)
    producto_id = models.ForeignKey('Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    actualizado = models.DateTimeField()
    
    def __str__(self):
        return f"{self.producto_id} {self.cantidad} {self.remito_id}"


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(30)
    modelo = models.CharField(50, unique=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"