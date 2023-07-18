from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_clientes, name="lista_clientes"),
    path("crear/", views.crear_cliente, name="crear_cliente"),
    path("editar/<str:cliente_id>/", views.editar_cliente, name="editar_cliente"),
    path("eliminar/<str:cliente_id>/", views.eliminar_cliente, name="eliminar_cliente"),
]
