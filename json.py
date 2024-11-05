import csv
import json

# Archivo CSV de entrada
csv_file_path = 'Libro1.csv'
# Archivo JSON de salida
json_file_path = 'cuentas.json'

# Lista para almacenar las cuentas
cuentas = []

# Lee el archivo CSV
with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        # Procesa cada fila del CSV
        codigo, nombre, tipo, _, nivel = row
        cuenta = {
            "codigo": codigo,
            "nombre": nombre,
            "tipo": tipo,
            "nivel": int(nivel),
            "parent": None if len(codigo) == 1 else codigo[:-1]
        }
        cuentas.append(cuenta)

# Escribe los datos en un archivo JSON
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(cuentas, json_file, indent=4, ensure_ascii=False)

print(f"Datos convertidos y guardados en {json_file_path}")