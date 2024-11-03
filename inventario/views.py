from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signin/')
def inicio(request):
    return render(request,"home.html")

# view de adquisicion de maretia prima
@login_required(login_url='/signin/')
def adquisicionMateriaPrima(request):
    return render(request,"adquisicion_materia.html")

# view de venta de producto
@login_required(login_url='/signin/')
def ventaProducto(request):
    return render(request,"venta_producto.html")

# view de inventario
@login_required(login_url='/signin/')
def manejoInventario(request):
    
    return render(request,"manejo_inventario.html")

#view de contratacion de personal
@login_required(login_url='/signin/')
def contratacion(request):
    return render(request,"contratacion.html")

#view de platilla general de empleados
@login_required(login_url='/signin/')
def plantillaGeneralEmpleados(request):
    return render(request,"plantilla_general_empreados.html")

