from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista_compras'),
    path('ingresar/', views.ingresar_compra, name='ingresar_compra'),
    path('detalle/<int:compra_id>/', views.detalle_compra, name='detalle_compra'),
    path('ingresar_item/<int:compra_id>/', views.ingresar_item, name='ingresar_item'),
    path('detalle_items/<int:compra_id>/items/', views.detalle_items_factura, name='detalle_items_factura'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('guardar/', views.guardar_compra, name='guardar_compra'),

]
