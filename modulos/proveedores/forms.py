from django import forms
from .models import Proveedores

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

