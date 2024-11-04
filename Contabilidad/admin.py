from django.contrib import admin

from Contabilidad.models import Cuenta, Periodo, Transaccion


admin.site.register(Cuenta)
admin.site.register(Periodo)
admin.site.register(Transaccion)
# Register your models here.
