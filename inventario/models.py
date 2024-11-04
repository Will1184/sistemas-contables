from django.db import models
from django.db import models

    
class ProductoAdquirido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)    
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    fecha_adquisicion = models.DateTimeField()    

    def __str__(self):
        return self.nombre

class ProductoVendido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    fecha_venta = models.DateField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=4, decimal_places=2, default=0.21)  # Por ejemplo, 21%

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} unidades"
    
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    dui = models.CharField(max_length=9, unique=True)  
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)  # Salario con dos decimales
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.puesto}"