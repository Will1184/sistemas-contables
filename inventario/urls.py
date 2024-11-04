# inventario/urls.py
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('adquisicionMaterial/', views.adquisicion_material,name='adquisicion_material'),
    path('editar_material/<int:producto_id>/', views.editar_material,name='editar_material'),
    path('editar_empleado/<int:empleado_id>/', views.editar_empleado,name='editar_empleado'),
    path('ventaProducto/', views.venta_producto, name='venta_producto'),
    path('ventasProductos/', views.ventas_productos, name='ventas_productos'),
    path('inventario/', views.manejo_inventario,name='manejo_inventario'),
    path('contratacion/', views.contratacion),
    path('plantillaGeneralEmpleados/', views.plantilla_general_empleados, name='plantilla_general_empleados'),     
]
