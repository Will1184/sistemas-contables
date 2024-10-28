from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('crearproducto/', views.crear_editar_producto, name='crear_producto'),
    path('editarProducto/<int:producto_id>/', views.crear_editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
