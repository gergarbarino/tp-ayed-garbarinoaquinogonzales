import csv
from pokemon import Pokemon


def cargar_catalogo(nombre_archivo):
    pokemons = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        next(lector)  # Saltea la primera fila, que es el encabezado

        for fila in lector:
            numero = int(fila[0])
            nombre = fila[1]
            tipo = fila[2]
            hp = int(fila[4])
            ataque = int(fila[5])
            defensa = int(fila[6])
            velocidad = int(fila[7])

            pokemon = Pokemon(
                numero,
                nombre,
                tipo,
                hp,
                ataque,
                defensa,
                velocidad
            )

            pokemons.append(pokemon)

    return pokemons
