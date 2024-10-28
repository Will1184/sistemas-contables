from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

productos = [
        {'id': 1, 'nombre': 'Producto 1', 'descripcion': 'Descripción del producto 1', 'precio': 10.99, 'cantidad': 5},
        {'id': 2, 'nombre': 'Producto 2', 'descripcion': 'Descripción del producto 2', 'precio': 15.50, 'cantidad': 3},
        {'id': 3, 'nombre': 'Producto 3', 'descripcion': 'Descripción del producto 3', 'precio': 7.75, 'cantidad': 10},
    ]
# Listar productos
def lista_productos(request):    
    return render(request, 'lista_productos.html', {'productos': productos})

# Vista para crear o editar un producto
def crear_editar_producto(request, producto_id=None):
    global productos

    # Si es una edición, buscamos el producto correspondiente
    if producto_id:
        producto = next((p for p in productos if p['id'] == producto_id), None)
        es_editar = True
    else:
        producto = {'id': len(productos) + 1, 'nombre': '', 'descripcion': '', 'precio': 0, 'cantidad': 0}
        es_editar = False

    # Manejo del formulario
    if request.method == 'POST':
        if es_editar:
            # Actualizar producto existente
            producto['nombre'] = request.POST['nombre']
            producto['descripcion'] = request.POST['descripcion']
            producto['precio'] = float(request.POST['precio'])
            producto['cantidad'] = int(request.POST['cantidad'])
        else:
            # Crear nuevo producto
            nuevos_datos = {
                'id': producto['id'],
                'nombre': request.POST['nombre'],
                'descripcion': request.POST['descripcion'],
                'precio': float(request.POST['precio']),
                'cantidad': int(request.POST['cantidad']),
            }
            productos.append(nuevos_datos)

        return redirect('lista_productos')

    return render(request, 'crear_editar_producto.html', {'producto': producto, 'es_editar': es_editar})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    global productos
    productos = [p for p in productos if p['id'] != producto_id]
    return redirect('lista_productos')