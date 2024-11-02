# inventario/urls.py
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('adquisicionMateriaPrima/', views.adquisicionMateriaPrima),
    path('ventaProducto/', views.ventaProducto),
    path('inventario/', views.manejoInventario),
    path('contratacion/', views.contratacion),
    path('plantillaGeneralEmpleados/', views.plantillaGeneralEmpleados),     
]
