from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_proveedores, name="lista_proveedores"),
    path("crear/", views.crear_proveedor, name="crear_proveedor"),
    path("editar/<str:proveedor_id>/", views.editar_proveedor, name="editar_proveedor"),
    path("eliminar/<str:proveedor_id>/", views.eliminar_proveedor, name="eliminar_proveedor"),
]
