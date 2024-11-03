# inventario/urls.py
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('adquisicionMateriaPrima/', views.adquisicionMateriaPrima, name='adquisicionMateriaPrima'),
    path('ventaProducto/', views.ventaProducto, name='ventaProducto'),
    path('inventario/', views.manejoInventario, name='inventario'),
    path('contratacion/', views.contratacion, name='contratacion'),
    path('plantillaGeneralEmpleados/', views.plantillaGeneralEmpleados, name='plantillaGeneralEmpleados'),     
]
