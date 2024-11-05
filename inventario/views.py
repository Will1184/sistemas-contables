import random
from .models  import ProductoAdquirido,Empleado, ProductoVendido
from Contabilidad.models import Cuenta,Transaccion,Periodo
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ProductoAdquiridoForm,ProductoVendidoForm,ProductoForm,EmpleadoForm
from datetime import datetime
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.

@login_required(login_url='/signin/')
def inicio(request):
    return render(request,"home.html")

@login_required(login_url='/signin/')
# view de inventario
def manejo_inventario(request):    
     productoss = ProductoAdquirido.objects.all()
     return render(request, 'manejo_inventario.html', {'productos': productoss})

@login_required(login_url='/signin/')
# view de adquisicion de material
def adquisicion_material(request):
       producto = {
            'id': "",  # Asignar un ID único basado en la longitud actual de la lista
            'nombre': '',
            'cantidad': '',
            'precio_compra': '',
            'fecha_adquisicion': datetime.now()
        }
       if request.method == 'POST':
        print(request.POST) 
        form = ProductoAdquiridoForm(request.POST)
        print(form.errors) 
        if form.is_valid():            
            compra=form.save(commit=False)          
            compra.precio_compra = compra.precio_unitario*compra.cantidad
            cuenta = Cuenta.objects.get(codigo = '11')         
            fecha = compra.fecha_adquisicion
            descripcion = "Adquisicion de Producto: "+ str(compra.nombre) + " Cantidad: "+ str(compra.cantidad)
            cuenta_debe = compra.precio_compra
            cuenta_haber = 0                     
            transaccion = Transaccion(cuenta_id=cuenta.id,periodo_id=1,fecha=fecha,descripcion=descripcion,debe=cuenta_debe,haber=cuenta_haber)
            transaccion.save()
            compra.save()
            return redirect('manejo_inventario')  
                
       return render(request,"adquisicion_material.html", {'producto': producto})

@login_required(login_url='/signin/')
def editar_material(request,producto_id):
    producto = get_object_or_404(ProductoAdquirido, id=producto_id)
    if request.method == 'POST':
        print(request.POST) 
        form = ProductoForm(request.POST, instance=producto)        
        if form.is_valid():
              form.save() 
              return redirect('manejo_inventario')         
    return render(request,"editar_material.html", {'producto':producto})

@login_required(login_url='/signin/')
def eliminar_material(request,producto_id):
    producto_adquirido = get_object_or_404(ProductoAdquirido, id=producto_id)    
    producto_adquirido.delete()    
    return redirect('manejo_inventario')        

@login_required(login_url='/signin/')
# view de venta de producto
def venta_producto(request):
    producto_vendido = {
            'id': 1, 
            'nombre': '',
            'cantidad': '',
            'precio_venta': '',
            'iva':'',
            'fecha_venta': datetime.now()
        }
    lista_productos = ProductoAdquirido.objects.filter(cantidad__gt=0)
    if request.method == 'POST':
        form = ProductoVendidoForm(request.POST)        
        producto_id = request.POST.get('nombre')
        cantidad_vendida = int(request.POST.get('cantidad'))        
        try:
            producto = ProductoAdquirido.objects.get(id=producto_id)
            if producto.cantidad >= cantidad_vendida:  
                print(form.data)      
                if form.is_valid():
                    venta = form.save(commit=False)
                    venta.iva= producto.iva
                    venta.nombre = producto.nombre
                    venta.precio_venta = Decimal(producto.precio_unitario )*Decimal((1 + producto.iva / 100))
                    venta.total = venta.precio_venta*venta.cantidad            
                    venta.fecha_venta = timezone.now() 
                    
                    cuenta = Cuenta.objects.get(codigo = '5101')         
                    fecha = venta.fecha_venta
                    descripcion = "Venta de Producto: "+ str(venta.nombre) + " Cantidad: "+ str(venta.cantidad)
                    cuenta_debe = venta.total
                    cuenta_haber = venta.total                    
                    transaccion = Transaccion(cuenta_id=cuenta.id,periodo_id=1,fecha=fecha,descripcion=descripcion,debe=cuenta_debe,haber=cuenta_haber)
                    transaccion.save()
                    
                    venta.save()                    

                    producto.cantidad -= cantidad_vendida
                    producto.save()
                    return redirect('ventas_productos')
                else:
                    error= form.errors
                    return render(request, 'venta_producto.html', {'producto': producto_vendido,'productos': lista_productos, 'error': error})
            else:
                error = "No hay suficiente cantidad disponible."
                return render(request, 'venta_producto.html', {'producto': producto_vendido,'productos': lista_productos, 'error': error})
        except ProductoAdquirido.DoesNotExist:
            error = "El producto seleccionado no existe."
            return render(request, 'venta_producto.html', {'producto': producto_vendido,'productos': lista_productos, 'error': error})                 
        
    return render(request,"venta_producto.html", {'producto': producto_vendido,'productos':lista_productos})

@login_required(login_url='/signin/')
def ventas_productos(request):
    productos = ProductoVendido.objects.all()
    return render(request,"ventas_productos.html",{'productos': productos}) 

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
         form = EmpleadoForm(request.POST)
         if form.is_valid():
              form.save() 
              return redirect('plantilla_general_empleados')  
    return render(request,"contratacion.html",{'contratacion_empleado': contratacion_empleado})

@login_required(login_url='/signin/')
def editar_empleado(request,empleado_id):
    contratacion_empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        print(request.POST) 
        form = EmpleadoForm(request.POST, instance=contratacion_empleado)        
        if form.is_valid():
              form.save() 
              return redirect('plantilla_general_empleados')         
    return render(request,"contratacion.html", {'contratacion_empleado':contratacion_empleado})

@login_required(login_url='/signin/')
def eliminar_empleado(request,empleado_id):
    contratacion_empleado = get_object_or_404(Empleado, id=empleado_id)    
    contratacion_empleado.delete()    
    return redirect('plantilla_general_empleados')             

@login_required(login_url='/signin/')
#view de platilla general de empleados
def plantilla_general_empleados(request):
    empleadoss = Empleado.objects.all()
    return render(request,"plantilla_general_empleados.html",{'empleados': empleadoss}) 

