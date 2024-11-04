# inventario/urls.py
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('adquisicionMaterial/', views.adquisicionMaterial,name='adquisicion_material'),
    path('ventaProducto/', views.ventaProducto),
    path('inventario/', views.manejo_inventario,name='manejo_inventario'),
    path('contratacion/', views.contratacion),
    path('plantillaGeneralEmpleados/', views.plantilla_general_empleados, name='plantilla_general_empleados'),     
]
