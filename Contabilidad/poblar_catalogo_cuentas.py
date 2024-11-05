import os
import django
from django.db import transaction, IntegrityError

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemas_contables.settings')
django.setup()

from Contabilidad.models import Cuenta  # Importa el modelo después de configurar el entorno

# Estructura completa del catálogo de cuentas
cuentas = [
    {"codigo": "1", "nombre": "Activo", "tipo": "ACTIVO", "nivel": 1, "parent": None},
    {"codigo": "11", "nombre": "Activo Corriente", "tipo": "ACTIVO", "nivel": 2, "parent": "1"},
    {"codigo": "1101", "nombre": "Caja y Bancos", "tipo": "ACTIVO", "nivel": 3, "parent": "11"},
    {"codigo": "110101", "nombre": "Caja General", "tipo": "ACTIVO", "nivel": 4, "parent": "1101"},
    {"codigo": "110102", "nombre": "Banco Nacional", "tipo": "ACTIVO", "nivel": 4, "parent": "1101"},
    {"codigo": "110103", "nombre": "Banco Internacional", "tipo": "ACTIVO", "nivel": 4, "parent": "1101"},
    {"codigo": "1102", "nombre": "Clientes", "tipo": "ACTIVO", "nivel": 3, "parent": "11"},
    {"codigo": "110201", "nombre": "Clientes Nacionales", "tipo": "ACTIVO", "nivel": 4, "parent": "1102"},
    {"codigo": "110202", "nombre": "Estimación de Cuentas Incobrables", "tipo": "ACTIVO", "nivel": 4, "parent": "1102"},
    {"codigo": "1103", "nombre": "Inventario de Productos Tecnológicos", "tipo": "ACTIVO", "nivel": 3, "parent": "11"},
    {"codigo": "110301", "nombre": "Computadoras de Escritorio", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110302", "nombre": "Laptops", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    # Continúa añadiendo las cuentas aquí
]

# Función para poblar el catálogo de cuentas
def poblar_cuentas():
    with transaction.atomic():  # Asegúrate de que todas las inserciones se realicen como una transacción
        for cuenta in cuentas:
            try:
                parent = None
                if cuenta["parent"]:
                    # Busca la cuenta padre
                    parent = Cuenta.objects.get(codigo=cuenta["parent"])
                # Crea la nueva cuenta
                Cuenta.objects.create(
                    codigo=cuenta["codigo"],
                    nombre=cuenta["nombre"],
                    tipo=cuenta["tipo"],
                    nivel=cuenta["nivel"],
                    parent=parent
                )
                print(f"Cuenta {cuenta['codigo']} - {cuenta['nombre']} creada con éxito.")
            except IntegrityError:
                print(f"La cuenta {cuenta['codigo']} ya existe. Omitiendo...")
            except Cuenta.DoesNotExist:
                print(f"La cuenta padre {cuenta['parent']} no existe. Omitiendo cuenta {cuenta['codigo']}.")
            except Exception as e:
                print(f"Error al crear la cuenta {cuenta['codigo']}: {e}")

if __name__ == "__main__":
    poblar_cuentas()
    print("Catálogo de cuentas poblado exitosamente.")  