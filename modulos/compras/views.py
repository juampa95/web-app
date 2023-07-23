from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect, get_object_or_404
from .models import Compra, DetalleCompra, Proveedores, Producto

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Compra, DetalleCompra, Proveedores, Producto
from decimal import Decimal

from django.shortcuts import render, redirect
from .models import Compra, DetalleCompra, Proveedores, Producto
from decimal import Decimal
import json

def ingresar_compra(request):
    # Obtener la lista de proveedores para mostrar en el formulario
    proveedores = Proveedores.objects.all()

    # Obtener la lista de productos para mostrar en el formulario
    productos = Producto.objects.all().values()

    if request.method == 'POST':
        # Obtener los datos del formulario de compra
        numero_factura = request.POST.get('numero_factura')
        proveedor_id = request.POST.get('proveedor_id')
        fecha = request.POST.get('fecha')

        # Crear la nueva compra en la base de datos
        proveedor = Proveedores.objects.get(pk=proveedor_id)
        nueva_compra = Compra.objects.create(numero_factura=numero_factura, proveedor=proveedor, fecha=fecha)

        # Obtener los detalles de la compra del formulario
        detalle_productos = request.POST.getlist('producto')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio')

        for i in range(len(detalle_productos)):
            producto = Producto.objects.get(pk=detalle_productos[i])
            cantidad = int(cantidades[i])
            precio = Decimal(precios[i])
            subtotal = cantidad * precio

            # Crear el detalle de compra y asociarlo a la nueva compra
            DetalleCompra.objects.create(compra=nueva_compra, producto=producto, cantidad=cantidad, precio=precio, subtotal=subtotal)

        # Actualizar el total de la compra
        nueva_compra.total = sum(detalle.subtotal for detalle in nueva_compra.detallecompra_set.all())
        nueva_compra.save()

        # Redireccionar a la página de detalles de la nueva compra
        return redirect('detalle_compra', compra_id=nueva_compra.id)

    return render(request, 'ingresar_compra.html', {'proveedores': proveedores, 'productos': json.dumps(list(productos), cls=DjangoJSONEncoder)})


def detalle_compra(request, compra_id):
    # Obtener la compra con el ID proporcionado
    compra = get_object_or_404(Compra, id=compra_id)

    return render(request, 'detalle_compra.html', {'compra': compra})


def lista_items_factura(request, compra_id):
    # Obtener la compra con el ID proporcionado
    compra = get_object_or_404(Compra, id=compra_id)

    return render(request, 'lista_items_factura.html', {'compra': compra})


def lista_compras(request):
    # Obtener todas las facturas de compra con sus detalles de proveedor
    facturas = Compra.objects.all().select_related('proveedor')

    return render(request, 'lista_compras.html', {'facturas': facturas})


