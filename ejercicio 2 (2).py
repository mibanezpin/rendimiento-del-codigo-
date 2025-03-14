import csv
import cProfile

def letra_dni(dni):
    if len(str(dni)) != 8:
        raise Exception("El DNI debe tener 8 dígitos")
    LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return f"{dni}{LETRAS_DNI[int(dni) % 23]}"

def capitalizar_nombre(nombre):
    return nombre.title()

def procesar_csv(archivo):
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar la cabecera
        datos = [(capitalizar_nombre(fila[0]), letra_dni(fila[1])) for fila in reader]
    return datos

def main():
    archivo_50 = 'personas_50.csv'
    archivo_1000 = 'personas_1000.csv'
    print(procesar_csv(archivo_50))
    print(procesar_csv(archivo_1000))

cProfile.run('main()')
