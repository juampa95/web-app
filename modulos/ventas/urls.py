from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ventas, name='lista_ventas'),
    path('crear/', views.crear_venta, name='crear_ventas'),
    path('editar/<int:venta_id>/', views.editar_venta, name='editar_ventas'),
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_ventas'),
    path('detalle/<int:venta_id>/', views.detalle_venta, name='detalle_ventas'),
]
