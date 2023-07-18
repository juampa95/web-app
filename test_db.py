from web_app.models import Cliente

# Obtener el modelo Cliente
modelo_cliente = Cliente

# Obtener los nombres de las columnas del modelo
nombres_columnas = [campo.name for campo in modelo_cliente._meta.get_fields()]

# Imprimir los nombres de las columnas
print(nombres_columnas)
