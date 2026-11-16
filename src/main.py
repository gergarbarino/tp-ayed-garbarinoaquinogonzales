from src.catalogo import cargar_catalogo
from src.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola

from src.excepciones import (
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
    ArchivoInvalidoError
)

from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

# E5: Persistencia de archivos
from src.dominio.pokedex import (
    armar_catalogo_desde_txt,
    filas_del_catalogo,
    ENCABEZADOS,
    RUTA_POKEDEX
)

from src.persistencia.texto import guardar_texto

from src.persistencia.binario import (
    guardar_binario,
    cargar_binario
)

# E5: Persistencia del equipo
from src.persistencia.equipo_archivo import (
    guardar_equipo_binario,
    cargar_equipo_binario,
    modificar_hp_equipo
)


# Catálogo inicial
catalogo = cargar_catalogo()

# E5: Ruta del archivo binario
RUTA_BIN = RUTA_POKEDEX.with_suffix(".bin")


def buscar_pokemon(catalogo):

    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")

    tipo = input("Elija opción: ").strip()

    print("1. Buscar por ID")
    print("2. Buscar por Nombre")

    criterio = input("Elija opción: ").strip()

    if criterio == "2":

        entrada = input("Ingrese el nombre del Pokémon: ").strip()

        clave = entrada.lower()
        obtener_clave = lambda p: p.nombre.lower()

    else:

        entrada = input("Ingrese el ID del Pokémon: ").strip()

        if not entrada.isdigit():

            print("Debe ingresar un ID numérico.")
            return True

        clave = int(entrada)
        obtener_clave = lambda p: p.numero

    if entrada.lower() == "apagar":
        return True

    datos = list(catalogo)

    if tipo == "2":

        datos = ordenar_insercion(datos, obtener_clave)

        indice = busqueda_binaria(
            datos,
            clave,
            obtener_clave
        )

    else:

        indice = busqueda_lineal(
            datos,
            clave,
            obtener_clave
        )

    if indice is not None:

        pokemon = datos[indice]

        print(f"¡Encontrado!: {pokemon}")

    else:

        print("No se encontró un Pokémon con ese dato.")

    return True


def menu_coleccion(equipo, pila_historial, cola_turnos, catalogo):

    while True:

        print("\n========== POKÉDEX ==========")
        print("1. Agregar al equipo")
        print("2. Listar equipo")
        print("3. Deshacer (pila)")
        print("4. Siguiente turno (cola)")
        print("5. Buscar Pokémon")
        print("6. Ordenar catálogo")
        print("7. Eliminar Pokémon del equipo")
        print("8. Modificar HP de un Pokémon")
        print("9. Guardar / cargar archivos")
        print("0. Salir")

        opcion = input("> ").strip()

        if opcion == "0":

            break

        elif opcion == "1":

            entrada = input("Ingrese el ID del Pokémon: ").strip()

            if entrada.isdigit():

                id_buscado = int(entrada)

                datos = list(catalogo)

                indice = busqueda_lineal(
                    datos,
                    id_buscado,
                    lambda p: p.numero
                )

                if indice is None:

                    print("No se encontró un Pokémon con ese ID.")

                else:

                    pokemon_encontrado = datos[indice]

                    try:

                        equipo.agregar(pokemon_encontrado)

                        guardar_equipo_binario(equipo)

                        print(f"Agregado: {pokemon_encontrado}")
                        print("Equipo guardado correctamente.")

                    except ColeccionLlenaError as e:

                        print(f"Error: {e}")

                    except (ArchivoInvalidoError, OSError) as e:

                        print(
                            f"El Pokémon se agregó al equipo, "
                            f"pero no se pudo guardar: {e}"
                        )

        elif opcion == "2":

            equipo.listar()

        elif opcion == "3":

            try:

                item = pila_historial.desapilar()

                print(f"Deshecho: {item}")

            except PilaVaciaError as e:

                print(f"Error: {e}")

        elif opcion == "4":

            try:

                item = cola_turnos.desencolar()

                print(f"Turno atendido: {item}")

            except ColaVaciaError as e:

                print(f"Error: {e}")

        elif opcion == "5":

            buscar_pokemon(catalogo)

        elif opcion == "6":

            print("1. Ordenar por ID (Selección)")
            print("2. Ordenar por Nombre (Inserción)")

            metodo = input("> ").strip()

            if metodo == "1":

                catalogo = ordenar_seleccion(
                    catalogo,
                    lambda p: p.numero
                )

                print("Catálogo ordenado por ID (Selección).")

            elif metodo == "2":

                catalogo = ordenar_insercion(
                    catalogo,
                    lambda p: p.nombre
                )

                print("Catálogo ordenado por Nombre (Inserción).")

        # E5: Eliminar un Pokémon del equipo
        elif opcion == "7":

            entrada = input("Ingrese el ID del Pokémon a eliminar: ").strip()

            if not entrada.isdigit():

                print("Debe ingresar un ID numérico.")

            else:

                id_buscado = int(entrada)

                pokemon_a_eliminar = None

                for pokemon in equipo:

                    if pokemon.numero == id_buscado:

                        pokemon_a_eliminar = pokemon
                        break

                if pokemon_a_eliminar is None:

                    print("Ese Pokémon no se encuentra en el equipo.")

                else:

                    equipo.eliminar(pokemon_a_eliminar)

                    try:

                        guardar_equipo_binario(equipo)

                        print(f"Pokémon eliminado: {pokemon_a_eliminar}")
                        print("Cambio guardado correctamente.")

                    except (ArchivoInvalidoError, OSError) as error:

                        print(
                            f"El Pokémon se eliminó del equipo, "
                            f"pero no se pudo guardar: {error}"
                        )

        # E5: Modificar el HP de un Pokémon del equipo
        elif opcion == "8":

            entrada = input("Ingrese el ID del Pokémon a modificar: ").strip()

            if not entrada.isdigit():

                print("Debe ingresar un ID numérico.")

            else:

                id_buscado = int(entrada)

                entrada_hp = input("Ingrese el nuevo HP: ").strip()

                if not entrada_hp.isdigit():

                    print("El HP debe ser un número entero positivo.")

                else:

                    nuevo_hp = int(entrada_hp)

                    try:

                        modificado = modificar_hp_equipo(
                            id_buscado,
                            nuevo_hp
                        )

                        if modificado:

                            # Recuperamos el equipo con los datos actualizados
                            equipo = cargar_equipo_binario()

                            print("HP modificado correctamente.")
                            print("Cambio guardado en el archivo binario.")

                        else:

                            print("Ese Pokémon no se encuentra en el equipo.")

                    except (ValueError, ArchivoInvalidoError, OSError) as error:

                        print(f"Error al modificar el Pokémon: {error}")

        # E5: Guardar y cargar archivos
        elif opcion == "9":

            print("\n--- Guardar / Cargar Archivos ---")
            print("1. Cargar catálogo desde TXT")
            print("2. Guardar catálogo en TXT")
            print("3. Guardar catálogo en binario")
            print("4. Cargar catálogo desde binario")
            print("0. Volver")

            subopcion = input("> ").strip()

            try:

                if subopcion == "1":

                    catalogo = armar_catalogo_desde_txt()

                    print(
                        f"Catálogo cargado desde TXT: "
                        f"{catalogo.tamanio()} Pokémon."
                    )

                elif subopcion == "2":

                    filas = filas_del_catalogo(catalogo)

                    guardar_texto(
                        RUTA_POKEDEX,
                        filas,
                        ENCABEZADOS
                    )

                    print("Catálogo guardado correctamente en TXT.")

                elif subopcion == "3":

                    guardar_binario(
                        RUTA_BIN,
                        catalogo
                    )

                    print("Catálogo guardado correctamente en binario.")

                elif subopcion == "4":

                    catalogo = cargar_binario(RUTA_BIN)

                    print(
                        f"Catálogo cargado desde binario: "
                        f"{catalogo.tamanio()} Pokémon."
                    )

                elif subopcion == "0":

                    continue

                else:

                    print("Opción inválida.")

            except ArchivoInvalidoError as error:

                print(f"Error de archivo: {error}")


# E5: Recuperar el equipo al iniciar el programa
try:

    equipo = cargar_equipo_binario()

except (ArchivoInvalidoError, OSError) as error:

    raise SystemExit(
        f"No se pudo recuperar el equipo guardado: {error}"
    )


pila_historial = Pila()
cola_turnos = Cola()

menu_coleccion(equipo, pila_historial, cola_turnos, catalogo)