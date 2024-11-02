from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"home.html")

# view de adquisicion de maretia prima
def adquisicionMateriaPrima(request):
    return render(request,"adquisicion_materia.html")

# view de venta de producto
def ventaProducto(request):
    return render(request,"venta_producto.html")

# view de inventario
def manejoInventario(request):
    return render(request,"manejo_inventario.html")

#view de contratacion de personal
def contratacion(request):
    return render(request,"contratacion.html")

#view de platilla general de empleados
def plantillaGeneralEmpleados(request):
    return render(request,"plantilla_general_empreados.html")

