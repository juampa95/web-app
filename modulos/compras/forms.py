from django import forms
from .models import Compra, DetalleCompra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['numero_factura', 'proveedor', 'fecha']

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'precio']

DetalleCompraFormset = forms.inlineformset_factory(Compra, DetalleCompra, form=DetalleCompraForm, extra=1)
