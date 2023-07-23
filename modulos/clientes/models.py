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
