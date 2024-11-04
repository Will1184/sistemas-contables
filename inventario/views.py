from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ProductoAdquiridoForm
import random
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
productos = [
    {
        "id": 1,
        "nombre": "Laptop",        
        "cantidad": random.randint(1, 100),
        "precio_unitario": round(random.uniform(300, 1500), 2),
        "precio_venta": round(random.uniform(500, 2000), 2),
        "precio_compra": round(random.uniform(200, 1200), 2),
        "fecha_adquisicion": datetime(2023, 1, 20, 14, 30)
    },
    {
        "id": 2,
        "nombre": "Monitor",        
        "cantidad": random.randint(1, 100),
        "precio_unitario": round(random.uniform(100, 300), 2),
        "precio_venta": round(random.uniform(150, 400), 2),
        "precio_compra": round(random.uniform(80, 250), 2),
        "fecha_adquisicion": datetime(2023, 2, 10, 10, 15)
    },
    {
        "id": 3,
        "nombre": "Teclado",        
        "cantidad": random.randint(1, 100),
        "precio_unitario": round(random.uniform(30, 100), 2),
        "precio_venta": round(random.uniform(50, 150), 2),
        "precio_compra": round(random.uniform(20, 80), 2),
        "fecha_adquisicion": datetime(2023, 3, 5, 9, 45)
    },
    {
        "id": 4,
        "nombre": "Memoria RAM",        
        "cantidad": random.randint(1, 100),
        "precio_unitario": round(random.uniform(60, 150), 2),
        "precio_venta": round(random.uniform(80, 200), 2),
        "precio_compra": round(random.uniform(50, 120), 2),
        "fecha_adquisicion": datetime(2023, 4, 12, 11, 30)
    },
    {
        "id": 5,
        "nombre": "Disco Duro",        
        "cantidad": random.randint(1, 100),
        "precio_unitario": round(random.uniform(50, 100), 2),
        "precio_venta": round(random.uniform(70, 130), 2),
        "precio_compra": round(random.uniform(40, 90), 2),
        "fecha_adquisicion": datetime(2023, 5, 22, 13, 0)
    }
]

empleados = [
    {
        "dui": "12345678-9",
        "nombres": "Juan",
        "apellidos": "Pérez",
        "puesto": "Gerente",
        "salario": 1500.00,
        "fecha_contratacion": datetime(2020, 1, 15)
    },
    {
        "dui": "98765432-1",
        "nombres": "Ana",
        "apellidos": "Gómez",
        "puesto": "Desarrolladora",
        "salario": 1200.00,
        "fecha_contratacion": datetime(2021, 5, 10)
    },
    {
        "dui": "11223344-5",
        "nombres": "Luis",
        "apellidos": "Martínez",
        "puesto": "Analista",
        "salario": 1000.00,
        "fecha_contratacion": datetime(2019, 8, 20)  
    },
    {
        "dui": "55667788-0",
        "nombres": "María",
        "apellidos": "López",
        "puesto": "Diseñadora",
        "salario": 1100.00,
        "fecha_contratacion": datetime(2022, 3, 15)
    },
    {
        "dui": "12344321-7",
        "nombres": "Carlos",
        "apellidos": "Reyes",
        "puesto": "Tester",
        "salario": 900.00,
        "fecha_contratacion": datetime(2023, 4, 1) 
    },
]

@login_required(login_url='/signin/')
def inicio(request):
    return render(request,"home.html")

@login_required(login_url='/signin/')
# view de inventario
def manejo_inventario(request):    
     return render(request, 'manejo_inventario.html', {'productos': productos})

@login_required(login_url='/signin/')
# view de adquisicion de material
def adquisicionMaterial(request):
       producto = {
            'id': len(productos) + 1,  # Asignar un ID único basado en la longitud actual de la lista
            'nombre': '',
            'cantidad': '',
            'precio_compra': '',
            'fecha_adquisicion': datetime.now()
        }
       if request.method == 'POST':
        print(request.POST) 
        nuevos_datos = {
                'id': producto['id'],
                'nombre': request.POST['nombre'],
                'fecha_adquisicion': request.POST['fecha_adquisicion'],
                'precio_compra': float(request.POST['precio_compra']),
                'cantidad': int(request.POST['cantidad']),
            }
        productos.append(nuevos_datos)
        return redirect('manejo_inventario')  
       return render(request,"adquisicion_material.html", {'producto': producto})

@login_required(login_url='/signin/')
# view de venta de producto
def ventaProducto(request):
    producto_vendido = {
            'id': 1, 
            'nombre': '',
            'cantidad': '',
            'precio_venta': '',
            'iva':'',
            'fecha_venta': datetime.now()
        }

    if request.method == 'POST':
        print(request.POST) 
        nuevos_datos =  {
            'id': producto_vendido['id'],
            'nombre':  request.POST['nombre'],
            'cantidad':  request.POST['cantidad'],
            'precio_venta':  request.POST['precio_venta'],
            'iva': request.POST['iva'],
            'fecha_venta':  request.POST['fecha_venta']
        }
        productos.append(nuevos_datos)
        return redirect('manejo_inventario')  
    return render(request,"venta_producto.html", {'producto': producto_vendido})

@login_required(login_url='/signin/')
#view de contratacion de personal
def contratacion(request):
    contratacion_empleado = {
        'id': 1,
        "dui": "",
        "nombres": "",
        "apellidos": "",
        "puesto": "",
        "salario": '',
        "fecha_contratacion": datetime.now() 
    }
    if request.method == 'POST':
        nuevos_datos =  {
            'id': contratacion_empleado['id'],
            "dui": request.POST['dui'],        
            'nombres':  request.POST['nombres'],
            "apellidos": request.POST['apellidos'],
            "puesto": request.POST['puesto'],
            "salario": request.POST['salario'],
            "fecha_contratacion": request.POST['fecha_contratacion'] 
        }
        empleados.append(nuevos_datos)
        return redirect('plantilla_general_empleados')  
    return render(request,"contratacion.html",{'empleado': contratacion_empleado})

@login_required(login_url='/signin/')
#view de platilla general de empleados
def plantilla_general_empleados(request):
    return render(request,"plantilla_general_empleados.html",{'empleados': empleados}) 
