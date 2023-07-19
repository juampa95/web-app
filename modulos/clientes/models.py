from django.db import models
from django.db.models import ProtectedError



class Cliente(models.Model):
    cliente_id = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    mov = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    @classmethod
    def crear_cliente(cls, cliente_id, nombre, email):
        cliente = cls(cliente_id=cliente_id, nombre=nombre, email=email)
        cliente.save()
        return cliente

    @classmethod
    def modificar_cliente(cls, cliente_id, nombre, email):
        cliente = cls.objects.get(cliente_id=cliente_id)
        cliente.nombre = nombre
        cliente.email = email
        cliente.save()
        return cliente

    @classmethod
    def eliminar_cliente(cls, cliente_id):
        cliente = cls.objects.get(cliente_id=cliente_id)
        if cliente.mov:
            raise ProtectedError("No se puede eliminar un cliente con movimiento de stock.", cliente)
        cliente.delete()


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