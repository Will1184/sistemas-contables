from django.contrib import admin

from inventario.models import ProductoAdquirido, ProductoVendido, Empleado


admin.site.register(ProductoAdquirido)
admin.site.register(ProductoVendido)
admin.site.register(Empleado)  
# Register your models here.
