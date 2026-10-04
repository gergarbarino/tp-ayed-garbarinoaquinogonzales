from src.pokemon import Pokemon
from src.tads.lista_enlazada import ListaEnlazada
import csv


def cargar_catalogo():
    archivo = open("data/pokedex.csv")
    lector = csv.reader(archivo)

    next(lector)

    catalogo = ListaEnlazada()

    for fila in lector:

        new_pokemon = Pokemon(

            int(fila[0]),
            fila[1],
            fila[2],
            fila[3],
            int(fila[4]),
            int(fila[5]),
            int(fila[6]),
            int(fila[7]),
            int(fila[8])
            )
        
        catalogo.agregar(new_pokemon)

    return catalogo