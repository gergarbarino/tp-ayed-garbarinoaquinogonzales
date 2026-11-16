from pathlib import Path

from src.persistencia.texto import cargar_texto


RAIZ = Path(__file__).resolve().parents[2]
RUTA_EVOLUCIONES = RAIZ / "data" / "evoluciones.csv"


def cargar_evoluciones():

    relaciones = {}

    filas = cargar_texto(RUTA_EVOLUCIONES)

    for fila in filas:

        origen = int(fila["origen_id"])
        destino = int(fila["destino_id"])

        if origen not in relaciones:

            relaciones[origen] = []

        relaciones[origen].append(destino)

    return relaciones


def mostrar_evoluciones_recursivas(
    id_pokemon,
    catalogo,
    relaciones,
    nivel=0
):

    nombre = None

    for pokemon in catalogo:

        if pokemon.numero == id_pokemon:

            nombre = pokemon.nombre
            break

    if nombre is None:

        print("  " * nivel + f"#{id_pokemon} (no figura en el catálogo)")

    else:

        print("  " * nivel + f"#{id_pokemon} {nombre}")

    # Caso base
    if id_pokemon not in relaciones:

        return

    # Caso recursivo
    for siguiente_id in relaciones[id_pokemon]:

        mostrar_evoluciones_recursivas(
            siguiente_id,
            catalogo,
            relaciones,
            nivel + 1
        )