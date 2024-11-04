import django
from django.db import transaction

# Configura el entorno de Django si es necesario
django.setup()

from Contabilidad.models import Cuenta  # Asegúrate de que 'Contabilidad' es el nombre correcto de tu aplicación

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
    {"codigo": "110303", "nombre": "Unidades de Procesamiento Central (CPU)", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110304", "nombre": "Unidades de Procesamiento Gráfico (GPU)", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110305", "nombre": "Memorias RAM", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110306", "nombre": "Discos Duros (HDD)", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110307", "nombre": "Unidades de Estado Sólido (SSD)", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110308", "nombre": "Monitores", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110309", "nombre": "Teclados", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110310", "nombre": "Ratones (Mouse)", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110311", "nombre": "Placas Madre", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110312", "nombre": "Fuentes de Poder", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "110313", "nombre": "Gabinetes (Cases)", "tipo": "ACTIVO", "nivel": 4, "parent": "1103"},
    {"codigo": "1104", "nombre": "IVA Crédito Fiscal", "tipo": "ACTIVO", "nivel": 3, "parent": "11"},
    {"codigo": "110401", "nombre": "IVA Crédito Fiscal", "tipo": "ACTIVO", "nivel": 4, "parent": "1104"},
    {"codigo": "1105", "nombre": "Anticipos a Proveedores", "tipo": "ACTIVO", "nivel": 3, "parent": "11"},
    {"codigo": "110501", "nombre": "Anticipo a Proveedores Nacionales", "tipo": "ACTIVO", "nivel": 4, "parent": "1105"},
    {"codigo": "110502", "nombre": "Anticipo a Proveedores Internacionales", "tipo": "ACTIVO", "nivel": 4, "parent": "1105"},
    
    {"codigo": "12", "nombre": "Activo No Corriente", "tipo": "ACTIVO", "nivel": 1, "parent": None},
    {"codigo": "1201", "nombre": "Propiedad, Planta y Equipo", "tipo": "ACTIVO", "nivel": 2, "parent": "12"},
    {"codigo": "120101", "nombre": "Mobiliario y Equipo de Oficina", "tipo": "ACTIVO", "nivel": 3, "parent": "1201"},
    {"codigo": "120102", "nombre": "Equipos de Computación", "tipo": "ACTIVO", "nivel": 3, "parent": "1201"},
    {"codigo": "120103", "nombre": "Herramientas de Reparación", "tipo": "ACTIVO", "nivel": 3, "parent": "1201"},
    {"codigo": "120104", "nombre": "Vehículos", "tipo": "ACTIVO", "nivel": 3, "parent": "1201"},
    {"codigo": "1202", "nombre": "Depreciación Acumulada", "tipo": "ACTIVO", "nivel": 2, "parent": "12"},
    {"codigo": "120201", "nombre": "Depreciación de Mobiliario y Equipo", "tipo": "ACTIVO", "nivel": 3, "parent": "1202"},
    {"codigo": "120202", "nombre": "Depreciación de Equipos de Computación", "tipo": "ACTIVO", "nivel": 3, "parent": "1202"},
    {"codigo": "120203", "nombre": "Depreciación de Vehículos", "tipo": "ACTIVO", "nivel": 3, "parent": "1202"},
    
    {"codigo": "21", "nombre": "Pasivo Corriente", "tipo": "PASIVO", "nivel": 1, "parent": None},
    {"codigo": "2101", "nombre": "Proveedores", "tipo": "PASIVO", "nivel": 2, "parent": "21"},
    {"codigo": "210101", "nombre": "Proveedores Nacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2101"},
    {"codigo": "210102", "nombre": "Proveedores Internacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2101"},
    {"codigo": "2102", "nombre": "Obligaciones Bancarias Corto Plazo", "tipo": "PASIVO", "nivel": 2, "parent": "21"},
    {"codigo": "210201", "nombre": "Préstamos Bancarios Nacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2102"},
    {"codigo": "210202", "nombre": "Préstamos Bancarios Internacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2102"},
    {"codigo": "2103", "nombre": "Retenciones por Pagar", "tipo": "PASIVO", "nivel": 2, "parent": "21"},
    {"codigo": "210301", "nombre": "Retención de ISR (Impuesto sobre la Renta)", "tipo": "PASIVO", "nivel": 3, "parent": "2103"},
    {"codigo": "210302", "nombre": "Retención de AFP (Administradora de Fondos de Pensiones)", "tipo": "PASIVO", "nivel": 3, "parent": "2103"},
    {"codigo": "210303", "nombre": "Retención de ISSS (Instituto Salvadoreño del Seguro Social)", "tipo": "PASIVO", "nivel": 3, "parent": "2103"},
    {"codigo": "2104", "nombre": "IVA Débito Fiscal", "tipo": "PASIVO", "nivel": 2, "parent": "21"},
    {"codigo": "210401", "nombre": "IVA Débito Fiscal", "tipo": "PASIVO", "nivel": 3, "parent": "2104"},
    {"codigo": "2105", "nombre": "Documentos por Pagar", "tipo": "PASIVO", "nivel": 2, "parent": "21"},
    {"codigo": "210501", "nombre": "Letras por Pagar Nacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2105"},
    {"codigo": "210502", "nombre": "Letras por Pagar Internacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2105"},
    
     # Pasivo No Corriente
    {"codigo": "22", "nombre": "Pasivo No Corriente", "tipo": "PASIVO", "nivel": 1, "parent": None},
    {"codigo": "2201", "nombre": "Obligaciones Bancarias Largo Plazo", "tipo": "PASIVO", "nivel": 2, "parent": "22"},
    {"codigo": "220101", "nombre": "Préstamos Hipotecarios", "tipo": "PASIVO", "nivel": 3, "parent": "2201"},
    {"codigo": "220102", "nombre": "Préstamos a Largo Plazo Nacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2201"},
    {"codigo": "220103", "nombre": "Préstamos a Largo Plazo Internacionales", "tipo": "PASIVO", "nivel": 3, "parent": "2201"},
    
    # Patrimonio
    {"codigo": "31", "nombre": "Capital y Reservas", "tipo": "PATRIMONIO", "nivel": 1, "parent": None},
    {"codigo": "3101", "nombre": "Capital Social", "tipo": "PATRIMONIO", "nivel": 2, "parent": "31"},
    {"codigo": "310101", "nombre": "Capital Suscrito", "tipo": "PATRIMONIO", "nivel": 3, "parent": "3101"},
    {"codigo": "310102", "nombre": "Capital Pagado", "tipo": "PATRIMONIO", "nivel": 3, "parent": "3101"},
    {"codigo": "3102", "nombre": "Reservas", "tipo": "PATRIMONIO", "nivel": 2, "parent": "31"},
    {"codigo": "310201", "nombre": "Reserva Legal", "tipo": "PATRIMONIO", "nivel": 3, "parent": "3102"},
    {"codigo": "310202", "nombre": "Reserva para Inversiones", "tipo": "PATRIMONIO", "nivel": 3, "parent": "3102"},
    {"codigo": "3103", "nombre": "Resultados Acumulados", "tipo": "PATRIMONIO", "nivel": 2, "parent": "31"},
    {"codigo": "310301", "nombre": "Utilidades Retenidas", "tipo": "PATRIMONIO", "nivel": 3, "parent": "3103"},
    {"codigo": "310302", "nombre": "Pérdidas Acumuladas", "tipo": "PATRIMONIO", "nivel": 3, "parent": "3103"},
    
    # Cuentas de Resultado Deudoras
    {"codigo": "41", "nombre": "Costos y Gastos de Operación", "tipo": "GASTO", "nivel": 1, "parent": None},
    {"codigo": "4101", "nombre": "Costo de Ventas", "tipo": "GASTO", "nivel": 2, "parent": "41"},
    {"codigo": "410101", "nombre": "Costo de Mercancía Vendida - Computadoras", "tipo": "GASTO", "nivel": 3, "parent": "4101"},
    {"codigo": "410102", "nombre": "Costo de Mercancía Vendida - Partes Tecnológicas", "tipo": "GASTO", "nivel": 3, "parent": "4101"},
    {"codigo": "410103", "nombre": "Costo de Mercancía Vendida - Accesorios", "tipo": "GASTO", "nivel": 3, "parent": "4101"},
    {"codigo": "4102", "nombre": "Gastos Administrativos", "tipo": "GASTO", "nivel": 2, "parent": "41"},
    {"codigo": "410201", "nombre": "Sueldos y Salarios Administrativos", "tipo": "GASTO", "nivel": 3, "parent": "4102"},
    {"codigo": "410202", "nombre": "Servicios Públicos (Agua, Luz, Teléfono, Internet)", "tipo": "GASTO", "nivel": 3, "parent": "4102"},
    {"codigo": "410203", "nombre": "Alquiler de Oficinas", "tipo": "GASTO", "nivel": 3, "parent": "4102"},
    {"codigo": "410204", "nombre": "Papelería y Útiles", "tipo": "GASTO", "nivel": 3, "parent": "4102"},
    {"codigo": "410205", "nombre": "Gastos de Mantenimiento y Reparación de Equipo", "tipo": "GASTO", "nivel": 3, "parent": "4102"},
    {"codigo": "4103", "nombre": "Gastos de Ventas", "tipo": "GASTO", "nivel": 2, "parent": "41"},
    {"codigo": "410301", "nombre": "Publicidad y Promoción", "tipo": "GASTO", "nivel": 3, "parent": "4103"},
    {"codigo": "410302", "nombre": "Comisiones de Venta", "tipo": "GASTO", "nivel": 3, "parent": "4103"},
    {"codigo": "410303", "nombre": "Transporte y Logística", "tipo": "GASTO", "nivel": 3, "parent": "4103"},
    {"codigo": "4104", "nombre": "Gastos Financieros", "tipo": "GASTO", "nivel": 2, "parent": "41"},
    {"codigo": "410401", "nombre": "Intereses sobre Préstamos", "tipo": "GASTO", "nivel": 3, "parent": "4104"},
    {"codigo": "410402", "nombre": "Comisiones Bancarias", "tipo": "GASTO", "nivel": 3, "parent": "4104"},
    
    # Otros Costos y Gastos
    {"codigo": "42", "nombre": "Otros Costos y Gastos", "tipo": "GASTO", "nivel": 1, "parent": None},
    {"codigo": "4201", "nombre": "Pérdidas en Venta de Activos Fijos", "tipo": "GASTO", "nivel": 2, "parent": "42"},
    {"codigo": "420101", "nombre": "Pérdida por Venta de Equipos de Computación", "tipo": "GASTO", "nivel": 3, "parent": "4201"},
    {"codigo": "420102", "nombre": "Pérdida por Venta de Vehículos", "tipo": "GASTO", "nivel": 3, "parent": "4201"},
    
    # Cuentas de Resultado Acreedoras
    {"codigo": "51", "nombre": "Ingresos por Ventas y Servicios", "tipo": "INGRESO", "nivel": 1, "parent": None},
    {"codigo": "5101", "nombre": "Ventas de Productos", "tipo": "INGRESO", "nivel": 2, "parent": "51"},
    {"codigo": "510101", "nombre": "Ventas de Computadoras de Escritorio", "tipo": "INGRESO", "nivel": 3, "parent": "5101"},
    {"codigo": "510102", "nombre": "Ventas de Laptops", "tipo": "INGRESO", "nivel": 3, "parent": "5101"},
    {"codigo": "510103", "nombre": "Ventas de Partes Tecnológicas (CPU, GPU, RAM, etc.)", "tipo": "INGRESO", "nivel": 3, "parent": "5101"},
    {"codigo": "510104", "nombre": "Ventas de Accesorios (Monitores, Teclados, Ratones)", "tipo": "INGRESO", "nivel": 3, "parent": "5101"},
    {"codigo": "5102", "nombre": "Servicios Prestados", "tipo": "INGRESO", "nivel": 2, "parent": "51"},
    {"codigo": "510201", "nombre": "Servicios de Reparación de Computadoras", "tipo": "INGRESO", "nivel": 3, "parent": "5102"},
    {"codigo": "510202", "nombre": "Servicios de Mantenimiento de Equipos de Computación", "tipo": "INGRESO", "nivel": 3, "parent": "5102"},
    
    # Otros Productos
    {"codigo": "52", "nombre": "Otros Productos", "tipo": "INGRESO", "nivel": 1, "parent": None},
    {"codigo": "5201", "nombre": "Ingresos Financieros", "tipo": "INGRESO", "nivel": 2, "parent": "52"},
    {"codigo": "520101", "nombre": "Intereses Ganados", "tipo": "INGRESO", "nivel": 3, "parent": "5201"},
    {"codigo": "520102", "nombre": "Ganancia por Diferencias Cambiarias", "tipo": "INGRESO", "nivel": 3, "parent": "5201"},
    
    # Cuentas de Cierre
    {"codigo": "61", "nombre": "Cuenta Liquidadora", "tipo": "CIE", "nivel": 1, "parent": None},
    {"codigo": "6101", "nombre": "Cierre de Ingresos", "tipo": "CIE", "nivel": 2, "parent": "61"},
    {"codigo": "610101", "nombre": "Cierre de Ventas de Productos", "tipo": "CIE", "nivel": 3, "parent": "6101"},
    {"codigo": "610102", "nombre": "Cierre de Servicios Prestados", "tipo": "CIE", "nivel": 3, "parent": "6101"},
    {"codigo": "6102", "nombre": "Cierre de Costos y Gastos", "tipo": "CIE", "nivel": 2, "parent": "61"},
    {"codigo": "610201", "nombre": "Cierre de Costos de Ventas", "tipo": "CIE", "nivel": 3, "parent": "6102"},
    {"codigo": "610202", "nombre": "Cierre de Gastos Administrativos", "tipo": "CIE", "nivel": 3, "parent": "6102"},
    
    # Cuentas de Orden
    {"codigo": "71", "nombre": "Cuentas de Orden", "tipo": "ORDEN", "nivel": 1, "parent": None},
    {"codigo": "7101", "nombre": "Mercancía en Consignación", "tipo": "ORDEN", "nivel": 2, "parent": "71"},
    {"codigo": "710101", "nombre": "Mercancía en Consignación Nacional", "tipo": "ORDEN", "nivel": 3, "parent": "7101"},
    {"codigo": "710102", "nombre": "Mercancía en Consignación Internacional", "tipo": "ORDEN", "nivel": 3, "parent": "7101"},
    {"codigo": "7102", "nombre": "Garantías Recibidas", "tipo": "ORDEN", "nivel": 2, "parent": "71"},
    {"codigo": "710201", "nombre": "Garantías de Clientes Nacionales", "tipo": "ORDEN", "nivel": 3, "parent": "7102"},
    {"codigo": "710202", "nombre": "Garantías de Clientes Internacionales", "tipo": "ORDEN", "nivel": 3, "parent": "7102"},
    
    {"codigo": "72", "nombre": "Cuentas de Orden por Contra", "tipo": "ORDEN", "nivel": 1, "parent": None},
    {"codigo": "7201", "nombre": "Mercancía en Consignación por Contra", "tipo": "ORDEN", "nivel": 2, "parent": "72"},
    {"codigo": "720101", "nombre": "Mercancía en Consignación por Contra Nacional", "tipo": "ORDEN", "nivel": 3, "parent": "7201"},
    {"codigo": "720102", "nombre": "Mercancía en Consignación por Contra Internacional", "tipo": "ORDEN", "nivel": 3, "parent": "7201"},
]

@transaction.atomic
def poblar_cuentas():
    cuentas_creadas = {}
    for cuenta in cuentas:
        parent = cuentas_creadas.get(cuenta["parent"]) if cuenta["parent"] else None
        nueva_cuenta = Cuenta.objects.create(
            codigo=cuenta["codigo"],
            nombre=cuenta["nombre"],
            tipo=cuenta["tipo"],
            nivel=cuenta["nivel"],
            parent=parent
        )
        cuentas_creadas[cuenta["codigo"]] = nueva_cuenta
        print(f"Cuenta creada: {nueva_cuenta.codigo} - {nueva_cuenta.nombre}")

# Ejecuta la función de carga de datos
poblar_cuentas()
