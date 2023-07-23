from django.db import models
from django.db.models import ProtectedError


class Producto(models.Model):
    item_id = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    mov = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    @classmethod
    def crear_producto(cls, item_id, nombre, precio):
        producto = cls(item_id=item_id, nombre=nombre, precio=precio)
        producto.save()
        return producto

    @classmethod
    def modificar_producto(cls, item_id, nombre, precio):
        producto = cls.objects.get(item_id=item_id)
        producto.nombre = nombre
        producto.precio = precio
        producto.save()
        return producto

    @classmethod
    def eliminar_producto(cls, item_id):
        producto = cls.objects.get(item_id=item_id)
        if producto.mov:
            raise ProtectedError("No se puede eliminar un producto con movimiento de stock.", producto)
        producto.delete()
