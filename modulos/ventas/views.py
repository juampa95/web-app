from django.shortcuts import render, redirect, get_object_or_404
from .models import Ventas
from .forms import VentasForm

def lista_ventas(request):
    ventas = Ventas.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            print("Venta creada correctamente")
            return redirect('lista_ventas')
    else:
        form = VentasForm()

    return render(request, 'crear_ventas.html', {'form': form})

def editar_venta(request, venta_id):
    venta = get_object_or_404(Ventas, pk=venta_id)
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentasForm(instance=venta)

    return render(request, 'editar_ventas.html', {'form': form})

def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Ventas, pk=venta_id)
    venta.delete()
    return redirect('lista_ventas')

def detalle_venta(request, venta_id):
    venta = get_object_or_404(Ventas, pk=venta_id)
    return render(request, 'detalle_ventas.html', {'venta': venta})
