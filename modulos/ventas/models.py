from django.db import models
from django.db.models import ProtectedError
from modulos.clientes.models import Cliente
from modulos.productos.models import Producto

class Ventas(models.Model):
    ventas_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cliente} - {self.producto}"

    def save(self, *args, **kwargs):
        # Actualiza el campo ha_tenido_movimiento en Cliente y Producto
        self.cliente.mov = True
        self.cliente.save()
        self.producto.mov = True
        self.producto.save()
        super().save(*args, **kwargs)
