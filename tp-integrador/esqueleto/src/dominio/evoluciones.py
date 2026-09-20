import csv


def cargar_evoluciones(nombre_archivo):
    evoluciones = []

    with open(nombre_archivo, "r") as archivo:
        lector = csv.reader(archivo)

        next(lector)

        for fila in lector:
            origen_id = int(fila[0])
            destino_id = int(fila[1])

            evoluciones.append([origen_id, destino_id])

    return evoluciones