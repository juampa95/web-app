from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista_compras'),
    path('ingresar/', views.ingresar_compra, name='ingresar_compra'),
    path('detalle/<int:compra_id>/', views.detalle_compra, name='detalle_compra'),
    path('lista/<int:compra_id>/', views.lista_items_factura, name='lista_compras'),

]
