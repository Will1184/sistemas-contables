from django.shortcuts import render, redirect
from django import forms
from datetime import date
from .models import ProductoAdquirido, ProductoVendido,Empleado

    
class ProductoAdquiridoForm(forms.ModelForm):
    class Meta:
        model = ProductoAdquirido
        fields = ['nombre', 'cantidad', 'precio_compra', 'fecha_adquisicion']

class ProductoVendidoForm(forms.ModelForm):
    class Meta:
        model = ProductoVendido
        fields = ['nombre', 'cantidad', 'precio_venta', 'iva',"fecha_venta"]

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['dui', 'nombres', 'apellidos', 'puesto', 'salario', 'fecha_contratacion']