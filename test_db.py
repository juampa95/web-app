from modulos.clientes.models import Cliente

# Obtener todos los registros de la base de datos
registros = Cliente.objects.all()

# Imprimir todos los campos y valores de cada registro
for registro in registros:
    print(registro.__dict__)