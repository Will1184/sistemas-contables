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

# en models.py
from django.db import models

class Periodo(models.Model):
    MESES = [
        (1, "Enero"),
        (2, "Febrero"),
        (3, "Marzo"),
        (4, "Abril"),
        (5, "Mayo"),
        (6, "Junio"),
        (7, "Julio"),
        (8, "Agosto"),
        (9, "Septiembre"),
        (10, "Octubre"),
        (11, "Noviembre"),
        (12, "Diciembre"),
    ]

    
    mes = models.PositiveSmallIntegerField(choices=MESES, default=1)  # Valor por defecto para mes
    ano = models.PositiveIntegerField(default=2024)  # Valor por defecto para año

    def __str__(self):
        return f"{self.get_mes_display()} {self.ano}"

    class Meta:
        verbose_name_plural = "Periodos"
        unique_together = ('mes', 'ano')  # Evita duplicados  # Evita que se dupliquen el mismo mes y año

# transacciones
class Transaccion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)  # Relación con el modelo Cuenta
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)  # Relación con el modelo Periodo
    fecha = models.DateField()
    debe = models.DecimalField(max_digits=10, decimal_places=2,default=0)  # Monto del debe
    haber = models.DecimalField(max_digits=10, decimal_places=2,default=0)  # Monto del haber
    descripcion = models.CharField(max_length=255, blank=True, null=True)  # Descripción opcional

    def __str__(self):
        return f"{self.descripcion} - Debe: {self.debe}, Haber: {self.haber} ({self.fecha})"

