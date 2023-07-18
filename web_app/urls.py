from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_clientes, name="lista_clientes"),
    path("crear/", views.crear_cliente, name="crear_cliente"),
]
