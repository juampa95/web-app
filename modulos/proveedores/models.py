from django.db import models
from django.db.models import ProtectedError

class Proveedores(models.Model):
    proveedor_id = models.CharField(primary_key=True, max_length=20)
    razon_social = models.CharField(max_length=100)
    cuit = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    mov = models.BooleanField(default=False)

    @classmethod
    def crear_proveedor(cls, proveedor_id, razon_social, cuit, email, telefono):
        proveedor = cls(proveedor_id=proveedor_id, razon_social=razon_social, cuit=cuit, email=email, telefono=telefono)
        proveedor.save()
        return proveedor

    @classmethod
    def modificar_proveedor(cls, proveedor_id, razon_social, cuit, email, telefono):
        proveedor = cls.objects.get(proveedor_id=proveedor_id)
        proveedor.razon_social = razon_social
        proveedor.cuit = cuit
        proveedor.email = email
        proveedor.telefono = telefono
        proveedor.save()
        return proveedor

    @classmethod
    def eliminar_proveedor(cls, proveedor_id):
        proveedor = cls.objects.get(proveedor_id=proveedor_id)
        if proveedor.mov:
            raise ProtectedError("No se puede eliminar un proveedor con movimientos asociados.", proveedor)
        proveedor.delete()
