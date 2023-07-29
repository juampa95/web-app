from django import forms
from .models import Cliente
import re

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente_id', 'nombre', 'apellido', 'email', 'telefono', 'regimen_afip']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Cambiar la etiqueta del campo cliente_id a 'Documento'
        self.fields['cliente_id'].label = 'Documento'
        self.fields['nombre'].label = 'Nombre'
        self.fields['apellido'].label = 'Apellido'

    def clean_cliente_id(self):
        regimen_afip = self.cleaned_data.get('regimen_afip')
        cliente_id = self.cleaned_data.get('cliente_id')

        if regimen_afip in ['RI', 'EX']:
            if not re.match(r'^\d{2}-\d{8}-\d$', cliente_id):
                raise forms.ValidationError('El CUIT/CUIL debe tener el formato __-________-_')
            return cliente_id
        else:
            # Verificar que el cliente_id sea numérico
            if not cliente_id.isdigit():
                raise forms.ValidationError('El DOCUMENTO debe ser numérico.')

            # Verificar la longitud del cliente_id
            if len(cliente_id) < 7 or len(cliente_id) > 8:
                raise forms.ValidationError('El DOCUMENTO debe tener entre 7 y 8 dígitos numéricos.')

            return cliente_id

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # transformamos el email en minusculas
        if email:
            email = email.lower()
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        apellido = self.cleaned_data.get('apellido')

        if nombre:
            nombre = nombre.lower()

        if apellido:
            apellido = apellido.lower()
        return nombre, apellido

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise forms.ValidationError('El telefono ingresado debe ser numérico.')






