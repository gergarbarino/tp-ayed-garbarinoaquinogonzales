from pathlib import Path
from src.excepciones import ArchivoInvalidoError


def cargar_csv(ruta):
    """Carga secuencial. Devuelve una lista de diccionarios."""

    return cargar_texto(ruta)


def guardar_csv(ruta, filas, encabezados):

    guardar_texto(ruta, filas, encabezados)


def cargar_texto(ruta):
    """Lee un archivo de texto y devuelve una lista de diccionarios."""

    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(
            f"No existe el archivo: {ruta}"
        )

    filas = []

    with ruta.open("r", encoding="utf-8") as archivo:

        encabezado = archivo.readline().strip().split(",")

        if encabezado == [""]:
            raise ArchivoInvalidoError("El archivo está vacío.")

        for linea in archivo:

            linea = linea.strip()

            if not linea:
                continue

            valores = linea.split(",")

            if len(valores) != len(encabezado):
                raise ArchivoInvalidoError(
                    "La cantidad de campos no coincide con el encabezado."
                )

            fila = dict(zip(encabezado, valores))

            filas.append(fila)

    return filas


def guardar_texto(ruta, filas, encabezados):
    """Guarda los registros en un archivo de texto."""

    ruta = Path(ruta)

    with ruta.open("w", encoding="utf-8", newline="") as archivo:

        archivo.write(",".join(encabezados) + "\n")

        for fila in filas:

            campos = [str(fila[clave]) for clave in encabezados]

            archivo.write(",".join(campos) + "\n")