from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedores
from .forms import ProveedoresForm

def lista_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedoresForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedores, proveedor_id=proveedor_id)
    if request.method == 'POST':
        form = ProveedoresForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedoresForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedores, proveedor_id=proveedor_id)
    proveedor.delete()
    return redirect('lista_proveedores')
