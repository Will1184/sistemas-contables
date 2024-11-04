from django.shortcuts import render, redirect
from django import forms
from datetime import date
from .models import ProductoAdquirido, ProductoVendido,Empleado

    
class ProductoAdquiridoForm(forms.ModelForm):
    class Meta:
        model = ProductoAdquirido
        fields = ['nombre', 'cantidad', 'precio_unitario', 'fecha_adquisicion']

class ProductoVendidoForm(forms.ModelForm):
    class Meta:
        model = ProductoVendido
        fields = ['nombre', 'cantidad']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['dui', 'nombres', 'apellidos', 'puesto', 'salario', 'fecha_contratacion']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoAdquirido
        fields = ['nombre', 'cantidad', 'precio_compra', 'precio_venta','fecha_adquisicion','precio_unitario']