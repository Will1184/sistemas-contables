from django.db import models

class Cuenta(models.Model):
    codigo = models.CharField(max_length=10, unique=True)  # Código de hasta 10 dígitos
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=[
        ('ACTIVO', 'Activo'),
        ('PASIVO', 'Pasivo'),
        ('PATRIMONIO', 'Patrimonio'),
        ('RESULTADO_DEUDOR', 'Cuentas de Resultado Deudoras'),
        ('RESULTADO_ACREEDOR', 'Cuentas de Resultado Acreedoras'),
        ('CIERRE', 'Cuenta de Cierre'),
        ('ORDEN', 'Cuentas de Orden')
    ])
    nivel = models.PositiveIntegerField()  # Para saber si es de 1, 2, 4, 6, 8 o 10 dígitos
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcuentas', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name_plural = "Cuentas"
# Create your models here.
