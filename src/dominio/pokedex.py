from pathlib import Path

from src.pokemon import Pokemon
from src.tads.lista_enlazada import ListaEnlazada
from src.persistencia.texto import cargar_texto


RAIZ = Path(__file__).resolve().parents[2]
RUTA_POKEDEX = RAIZ / "data" / "pokedex.txt"

ENCABEZADOS = [
    "id",
    "nombre",
    "tipo1",
    "tipo2",
    "hp",
    "ataque",
    "defensa",
    "velocidad",
    "generacion"
]


def armar_catalogo_desde_txt():

    catalogo = ListaEnlazada()

    filas = cargar_texto(RUTA_POKEDEX)

    for fila in filas:

        pokemon = Pokemon(
            numero=int(fila["id"]),
            nombre=fila["nombre"],
            tipo1=fila["tipo1"],
            tipo2=fila["tipo2"],
            hp=int(fila["hp"]),
            ataque=int(fila["ataque"]),
            defensa=int(fila["defensa"]),
            velocidad=int(fila["velocidad"]),
            generation=int(fila["generacion"])
        )

        catalogo.insertar_al_final(pokemon)

    return catalogo

def filas_del_catalogo(catalogo):

    filas = []

    for pokemon in catalogo:

        fila = {
            "id": pokemon.numero,
            "nombre": pokemon.nombre,
            "tipo1": pokemon.tipo1,
            "tipo2": pokemon.tipo2 or "",
            "hp": pokemon.hp,
            "ataque": pokemon.ataque,
            "defensa": pokemon.defensa,
            "velocidad": pokemon.velocidad,
            "generacion": pokemon.generation
        }

        filas.append(fila)

    return filas