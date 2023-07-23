from django import forms
from .models import Ventas
from modulos.clientes.models import Cliente
from modulos.productos.models import Producto

class VentasForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())

    class Meta:
        model = Ventas
        fields = ['cliente', 'producto', 'cantidad']
        exclude = ['fecha']
