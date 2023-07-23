from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_productos, name="lista"),
    path("crear/", views.crear_producto, name="crear"),  # Corregir esta línea
    path("editar/<str:item_id>/", views.editar_producto, name="editar"),
    path("eliminar/<str:item_id>/", views.eliminar_producto, name="eliminar"),
]
