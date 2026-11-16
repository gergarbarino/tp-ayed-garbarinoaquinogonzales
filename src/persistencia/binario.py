import struct
from pathlib import Path

from src.pokemon import Pokemon
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ArchivoInvalidoError


# Formato de cada Pokémon: 58 bytes
FORMATO = struct.Struct("<I 20s 12s 12s 5H")

# Cabecera del archivo: 9 bytes
HEADER = struct.Struct("<4s 1s I")

# Identificador de la Pokédex
TEMA = b"P"


def _a_bytes(texto, ancho):
    """Convierte un texto en bytes de longitud fija."""

    datos = texto.encode("utf-8")

    if len(datos) > ancho:
        raise ArchivoInvalidoError(
            f"El texto '{texto}' supera los {ancho} bytes permitidos."
        )

    return datos.ljust(ancho, b"\x00")


def _a_texto(datos):
    """Convierte bytes en texto."""

    return datos.rstrip(b"\x00").decode("utf-8")


def _item_a_tupla(pokemon):
    """Prepara los atributos del Pokémon para guardarlos."""

    return (
        pokemon.numero,
        _a_bytes(pokemon.nombre, 20),
        _a_bytes(pokemon.tipo1, 12),
        _a_bytes(pokemon.tipo2 or "", 12),
        pokemon.hp,
        pokemon.ataque,
        pokemon.defensa,
        pokemon.velocidad,
        pokemon.generation
    )


def _tupla_a_item(datos):
    """Convierte los datos binarios en un objeto Pokémon."""

    return Pokemon(
        numero=datos[0],
        nombre=_a_texto(datos[1]),
        tipo1=_a_texto(datos[2]),
        tipo2=_a_texto(datos[3]),
        hp=datos[4],
        ataque=datos[5],
        defensa=datos[6],
        velocidad=datos[7],
        generation=datos[8]
    )


def guardar_binario(ruta, items):
    """Guarda los Pokémon en un archivo binario."""

    registros = list(items)

    ruta = Path(ruta)

    with ruta.open("wb") as archivo:

        archivo.write(
            HEADER.pack(b"AYED", TEMA, len(registros))
        )

        for pokemon in registros:

            datos = _item_a_tupla(pokemon)

            archivo.write(
                FORMATO.pack(*datos)
            )


def cargar_binario(ruta):
    """Carga los Pokémon desde un archivo binario."""

    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(
            f"No existe el archivo: {ruta}"
        )

    with ruta.open("rb") as archivo:

        cabecera = archivo.read(HEADER.size)

        if len(cabecera) != HEADER.size:
            raise ArchivoInvalidoError(
                "El archivo binario tiene una cabecera incompleta."
            )

        magia, tema, cantidad = HEADER.unpack(cabecera)

        if magia != b"AYED":
            raise ArchivoInvalidoError(
                "La identificación del archivo es incorrecta."
            )

        if tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo no corresponde a una Pokédex."
            )

        catalogo = ListaEnlazada()

        for i in range(cantidad):

            registro = archivo.read(FORMATO.size)

            if len(registro) != FORMATO.size:
                raise ArchivoInvalidoError(
                    "El archivo binario tiene registros incompletos."
                )

            try:
                datos = FORMATO.unpack(registro)
                pokemon = _tupla_a_item(datos)

            except (UnicodeDecodeError, ValueError, struct.error) as error:
                raise ArchivoInvalidoError(
                    "El archivo contiene datos inválidos."
                ) from error

            catalogo.insertar_al_final(pokemon)

        if archivo.read(1):
            raise ArchivoInvalidoError(
                "El archivo contiene datos adicionales inesperados."
            )

    return catalogo


def actualizar_registro(ruta, posicion, item):
    """Modifica un Pokémon directamente en el archivo binario."""

    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(
            f"No existe el archivo: {ruta}"
        )

    datos = FORMATO.pack(*_item_a_tupla(item))

    with ruta.open("r+b") as archivo:

        cabecera = archivo.read(HEADER.size)

        if len(cabecera) != HEADER.size:
            raise ArchivoInvalidoError(
                "El archivo tiene una cabecera incompleta."
            )

        magia, tema, cantidad = HEADER.unpack(cabecera)

        if magia != b"AYED" or tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo binario no corresponde a esta Pokédex."
            )

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(
                "La posición indicada no existe."
            )

        archivo.seek(0, 2)

        tamanio_real = archivo.tell()
        tamanio_esperado = HEADER.size + cantidad * FORMATO.size

        if tamanio_real != tamanio_esperado:
            raise ArchivoInvalidoError(
                "El tamaño del archivo binario es incorrecto."
            )

        posicion_byte = HEADER.size + posicion * FORMATO.size

        archivo.seek(posicion_byte)

        archivo.write(datos)

def alta_binario(ruta, item):
    """Agrega un Pokémon al final del archivo binario."""

    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(
            f"No existe el archivo: {ruta}"
        )

    datos = FORMATO.pack(*_item_a_tupla(item))

    with ruta.open("r+b") as archivo:

        cabecera = archivo.read(HEADER.size)

        if len(cabecera) != HEADER.size:
            raise ArchivoInvalidoError(
                "La cabecera del archivo está incompleta."
            )

        magia, tema, cantidad = HEADER.unpack(cabecera)

        if magia != b"AYED" or tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo no corresponde a esta Pokédex."
            )

        archivo.seek(0, 2)

        tamanio_real = archivo.tell()
        tamanio_esperado = HEADER.size + cantidad * FORMATO.size

        if tamanio_real != tamanio_esperado:
            raise ArchivoInvalidoError(
                "El tamaño del archivo binario es incorrecto."
            )

        archivo.write(datos)

        archivo.seek(0)

        archivo.write(
            HEADER.pack(magia, tema, cantidad + 1)
        )

def baja_binario(ruta, posicion):
    """Elimina un Pokémon del archivo binario."""

    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(
            f"No existe el archivo: {ruta}"
        )

    with ruta.open("r+b") as archivo:

        cabecera = archivo.read(HEADER.size)

        if len(cabecera) != HEADER.size:
            raise ArchivoInvalidoError(
                "La cabecera del archivo está incompleta."
            )

        magia, tema, cantidad = HEADER.unpack(cabecera)

        if magia != b"AYED" or tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo no corresponde a esta Pokédex."
            )

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(
                "La posición indicada no existe."
            )

        registros = []

        for i in range(cantidad):

            datos = archivo.read(FORMATO.size)

            if len(datos) != FORMATO.size:
                raise ArchivoInvalidoError(
                    "El archivo tiene registros incompletos."
                )

            if i != posicion:
                registros.append(datos)

        if archivo.read(1):
            raise ArchivoInvalidoError(
                "El archivo contiene datos adicionales inesperados."
            )

        archivo.seek(0)

        archivo.write(
            HEADER.pack(magia, tema, cantidad - 1)
        )

        for datos in registros:
            archivo.write(datos)

        archivo.truncate()