from pathlib import Path

from src.equipo import Equipo
from src.pokemon import Pokemon

from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    actualizar_registro
)


RAIZ = Path(__file__).resolve().parents[2]
RUTA_EQUIPO = RAIZ / "data" / "equipo.bin"


def guardar_equipo_binario(equipo, ruta=RUTA_EQUIPO):

    guardar_binario(ruta, equipo)


def cargar_equipo_binario(ruta=RUTA_EQUIPO):

    equipo = Equipo()

    if not Path(ruta).exists():
        return equipo

    pokemones = cargar_binario(ruta)

    for pokemon in pokemones:
        equipo.agregar(pokemon)

    return equipo


def modificar_hp_equipo(id_buscado, nuevo_hp, ruta=RUTA_EQUIPO):

    if nuevo_hp < 1 or nuevo_hp > 65535:
        raise ValueError("El HP debe estar entre 1 y 65535.")

    equipo = cargar_equipo_binario(ruta)

    for posicion, pokemon in enumerate(equipo):

        if pokemon.numero == id_buscado:

            pokemon_actualizado = Pokemon(
                numero=pokemon.numero,
                nombre=pokemon.nombre,
                tipo1=pokemon.tipo1,
                tipo2=pokemon.tipo2,
                hp=nuevo_hp,
                ataque=pokemon.ataque,
                defensa=pokemon.defensa,
                velocidad=pokemon.velocidad,
                generation=pokemon.generation
            )

            actualizar_registro(
                ruta,
                posicion,
                pokemon_actualizado
            )

            return True

    return False