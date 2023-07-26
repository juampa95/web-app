from django.shortcuts import render, redirect, get_object_or_404
from .models import Compra, DetalleCompra, Producto, Proveedores
from .forms import CompraForm, DetalleCompraFormset
from decimal import Decimal
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
# from modulos.productos.models import Producto
# from modulos.proveedores.models import Proveedores
import json
from django.views.decorators.csrf import csrf_exempt

def lista_compras(request):
    compras = Compra.objects.all()
    return render(request, 'lista_compras.html', {'compras': compras})


def ingresar_compra(request):
    productos_disponibles = Producto.objects.all()
    proveedores = Proveedores.objects.all()
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            detalles_compra = []
            detalle_formset = DetalleCompraFormset(request.POST, instance=compra)
            if detalle_formset.is_valid():
                for form in detalle_formset:
                    detalle = form.save(commit=False)
                    detalle.compra = compra
                    detalle.save()
                    detalles_compra.append({
                        'producto_id': detalle.producto.id,
                        'cantidad': detalle.cantidad,
                        'precio': detalle.precio,
                        'subtotal': detalle.cantidad * detalle.precio
                    })

            # Retornar un JSON con el ID de la compra y los detalles de compra
            return JsonResponse({'compra_id': compra.id, 'detalles_compra': detalles_compra})
    else:
        form = CompraForm()

    return render(request, 'ingresar_compra.html', {'form': form,
                                                    'proveedores': proveedores,
                                                    'productos_disponibles': productos_disponibles})


def detalle_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    return render(request, 'detalle_compra.html', {'compra': compra})


def ingresar_item(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)

    if request.method == 'POST':
        formset = DetalleCompraFormset(request.POST, instance=compra)
        if formset.is_valid():
            formset.save()

            # Calcular los subtotales para cada detalle de compra y actualizarlos
            detalles = compra.detallecompra_set.all()
            for detalle in detalles:
                detalle.subtotal = detalle.cantidad * detalle.precio
                detalle.save()

            # Actualizar el total de la compra
            compra.total = sum(detalle.subtotal for detalle in detalles)
            compra.save()

            return redirect('detalle_compra', compra_id=compra.id)
    else:
        formset = DetalleCompraFormset(instance=compra)

    return render(request, 'ingresar_item.html', {'compra': compra, 'formset': formset})


def detalle_items_factura(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    detalles = DetalleCompra.objects.filter(compra=compra)
    return render(request, 'detalle_items_factura.html', {'compra': compra, 'detalles': detalles})


def lista_productos(request):
    productos = Producto.objects.all().values('item_id', 'nombre')
    return JsonResponse(list(productos), safe=False)

@csrf_exempt
def guardar_compra(request):
    print("Guardando compra")
    if request.method == 'POST':
        # Obtener los datos enviados desde el cliente
        numero_factura = request.POST.get('numero_factura')
        proveedor_id = request.POST.get('proveedor_id')
        fecha = request.POST.get('fecha')
        detalles = request.POST.getlist('detalles')

        # Crear una nueva instancia de la compra y guardarla en la base de datos

        nueva_compra = Compra.objects.create(numero_factura=numero_factura, proveedor=proveedor_id, fecha=fecha)

        # Ahora procesa los datos de los productos y crea y guarda los detalles de compra
        for detalle in detalles:
            producto_id = detalle['item_id']
            cantidad = detalle['cantidad']
            precio = detalle['precio']

            # Aquí puedes obtener el producto desde la base de datos
            producto = Producto.objects.get(pk=producto_id)

            # Calcular el subtotal
            subtotal = Decimal(cantidad) * Decimal(precio)

            # Crear el detalle de compra y asociarlo a la nueva compra
            DetalleCompra.objects.create(compra=nueva_compra, producto=producto, cantidad=cantidad, precio=precio,
                                         subtotal=subtotal)

        # Actualizar el total de la compra
        nueva_compra.total = sum(detalle.subtotal for detalle in nueva_compra.detallecompra_set.all())
        nueva_compra.save()
        print("aca esta la info si es que se guardo")
        print(request.POST)

        # Finalmente, envía una respuesta JSON al cliente indicando que la compra se ha guardado correctamente.
        return JsonResponse({'mensaje': 'Compra guardada exitosamente'})
        # return HttpResponse('Factura guardada con éxito')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
        # return HttpResponseBadRequest('Error al guardar la factura')
