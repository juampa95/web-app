from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm



def lista_productos(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'lista.html', {'productos': productos, 'form': form})



def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Producto guardado correctamente")
            return redirect('lista')
    else:
        form = ProductoForm()

    return render(request, 'crear.html', {'form': form})

def editar_producto(request, item_id):
    producto = get_object_or_404(Producto, pk=item_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar.html', {'form': form})



def eliminar_producto(request, item_id):
    cliente = get_object_or_404(Producto, pk=item_id)
    cliente.delete()
    return redirect('lista')
