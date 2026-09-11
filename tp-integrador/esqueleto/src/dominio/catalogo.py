import csv
from pokemon import Pokemon


def cargar_catalogo(pokedex):
    pokemons = []

    with open(pokedex, "r") as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            print(fila)

    return pokemons