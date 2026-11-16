from src.catalogo import cargar_catalogo
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

from src.dominio.listado import listar_catalogo, ver_detalle

# E2: Recursividad de evoluciones
from src.dominio.evoluciones import (
    cargar_evoluciones,
    mostrar_evoluciones_recursivas
)

# E5: Persistencia de archivos
from src.dominio.pokedex import (
    armar_catalogo_desde_txt,
    filas_del_catalogo,
    ENCABEZADOS,
    RUTA_POKEDEX
)

from src.persistencia.texto import guardar_texto
from src.persistencia.binario import guardar_binario, cargar_binario

from src.persistencia.equipo_archivo import (
    guardar_equipo_binario,
    cargar_equipo_binario,
    modificar_hp_equipo
)


catalogo = cargar_catalogo()

RUTA_BIN = RUTA_POKEDEX.with_suffix(".bin")


def obtener_pokemon_por_id(catalogo, id_buscado):

    datos = list(catalogo)

    indice = busqueda_lineal(
        datos,
        id_buscado,
        lambda p: p.numero
    )

    if indice is None:
        return None

    return datos[indice]


def buscar_pokemon(catalogo):

    print("\n1. Búsqueda Lineal")
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
            return

        clave = int(entrada)
        obtener_clave = lambda p: p.numero

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

        print(f"¡Encontrado!: {datos[indice]}")

    else:

        print("No se encontró un Pokémon con ese dato.")


def menu_equipo(equipo, catalogo):

    while True:

        print("\n========== ADMINISTRAR EQUIPO ==========")
        print("1. Agregar Pokémon")
        print("2. Listar equipo")
        print("3. Eliminar Pokémon")
        print("4. Modificar HP")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":

            return equipo

        elif opcion == "1":

            entrada = input("Ingrese el ID del Pokémon: ").strip()

            if not entrada.isdigit():

                print("Debe ingresar un ID numérico.")
                continue

            id_buscado = int(entrada)

            pokemon = obtener_pokemon_por_id(catalogo, id_buscado)

            if pokemon is None:

                print("No se encontró un Pokémon con ese ID.")

            else:

                try:

                    equipo.agregar(pokemon)

                    guardar_equipo_binario(equipo)

                    print(f"Agregado: {pokemon}")
                    print("Equipo guardado correctamente.")

                except ColeccionLlenaError as error:

                    print(f"Error: {error}")

                except (ArchivoInvalidoError, OSError) as error:

                    print(f"No se pudo guardar el equipo: {error}")

        elif opcion == "2":

            equipo.listar()

        elif opcion == "3":

            entrada = input("Ingrese el ID del Pokémon a eliminar: ").strip()

            if not entrada.isdigit():

                print("Debe ingresar un ID numérico.")
                continue

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

                    print(f"No se pudo guardar el cambio: {error}")

        elif opcion == "4":

            entrada = input("Ingrese el ID del Pokémon a modificar: ").strip()

            if not entrada.isdigit():

                print("Debe ingresar un ID numérico.")
                continue

            id_buscado = int(entrada)

            entrada_hp = input("Ingrese el nuevo HP: ").strip()

            if not entrada_hp.isdigit():

                print("El HP debe ser un número entero positivo.")
                continue

            nuevo_hp = int(entrada_hp)

            try:

                modificado = modificar_hp_equipo(
                    id_buscado,
                    nuevo_hp
                )

                if modificado:

                    equipo = cargar_equipo_binario()

                    print("HP modificado correctamente.")
                    print("Cambio guardado en el archivo binario.")

                else:

                    print("Ese Pokémon no se encuentra en el equipo.")

            except (ValueError, ArchivoInvalidoError, OSError) as error:

                print(f"Error al modificar el Pokémon: {error}")

        else:

            print("Opción inválida.")


def menu_archivos(catalogo):

    print("\n========== ARCHIVOS ==========")
    print("1. Cargar catálogo desde TXT")
    print("2. Guardar catálogo en TXT")
    print("3. Guardar catálogo en binario")
    print("4. Cargar catálogo desde binario")
    print("0. Volver")

    opcion = input("> ").strip()

    try:

        if opcion == "1":

            catalogo = armar_catalogo_desde_txt()

            print(
                f"Catálogo cargado desde TXT: "
                f"{catalogo.tamanio()} Pokémon."
            )

        elif opcion == "2":

            filas = filas_del_catalogo(catalogo)

            guardar_texto(
                RUTA_POKEDEX,
                filas,
                ENCABEZADOS
            )

            print("Catálogo guardado correctamente en TXT.")

        elif opcion == "3":

            guardar_binario(
                RUTA_BIN,
                catalogo
            )

            print("Catálogo guardado correctamente en binario.")

        elif opcion == "4":

            catalogo = cargar_binario(RUTA_BIN)

            print(
                f"Catálogo cargado desde binario: "
                f"{catalogo.tamanio()} Pokémon."
            )

        elif opcion != "0":

            print("Opción inválida.")

    except ArchivoInvalidoError as error:

        print(f"Error de archivo: {error}")

    return catalogo


def menu_principal(equipo, pila_historial, cola_turnos, catalogo):

    while True:

        print("\n========== POKÉDEX ==========")
        print("1. Listar catálogo")
        print("2. Ver detalle de un Pokémon")
        print("3. Buscar Pokémon")
        print("4. Ordenar catálogo")
        print("5. Evoluciones (recursividad)")
        print("6. Administrar equipo")
        print("7. Historial (pila)")
        print("8. Turnos (cola)")
        print("9. Guardar / cargar archivos")
        print("0. Salir")

        opcion = input("> ").strip()

        if opcion == "0":

            break

        elif opcion == "1":

            listar_catalogo(catalogo)

        elif opcion == "2":

            entrada = input("Ingrese el ID del Pokémon: ").strip()

            try:

                id_buscado = int(entrada)

                ver_detalle(catalogo, id_buscado)

            except ValueError:

                print("Debe ingresar un ID numérico.")

        elif opcion == "3":

            buscar_pokemon(catalogo)

        elif opcion == "4":

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

            else:

                print("Opción inválida.")

        # E2: Recursividad
        elif opcion == "5":

            entrada = input("Ingrese el ID del Pokémon: ").strip()

            if not entrada.isdigit():

                print("Debe ingresar un ID numérico.")

            else:

                id_buscado = int(entrada)

                pokemon = obtener_pokemon_por_id(
                    catalogo,
                    id_buscado
                )

                if pokemon is None:

                    print("No se encontró un Pokémon con ese ID.")

                else:

                    try:

                        relaciones = cargar_evoluciones()

                        print("\n========== EVOLUCIONES ==========")

                        mostrar_evoluciones_recursivas(
                            id_buscado,
                            catalogo,
                            relaciones
                        )

                    except (
                        ArchivoInvalidoError,
                        OSError,
                        ValueError,
                        KeyError
                    ) as error:

                        print(f"Error al cargar evoluciones: {error}")

        # E5: ABM persistente
        elif opcion == "6":

            equipo = menu_equipo(equipo, catalogo)

        # E6: Pila
        elif opcion == "7":

            print("\n========== HISTORIAL (PILA) ==========")
            print("1. Apilar Pokémon")
            print("2. Desapilar Pokémon")
            print("0. Volver")

            accion = input("> ").strip()

            if accion == "1":

                entrada = input("Ingrese el ID del Pokémon: ").strip()

                if not entrada.isdigit():

                    print("Debe ingresar un ID numérico.")

                else:

                    id_buscado = int(entrada)

                    pokemon = obtener_pokemon_por_id(
                        catalogo,
                        id_buscado
                    )

                    if pokemon is None:

                        print("No se encontró un Pokémon con ese ID.")

                    else:

                        pila_historial.apilar(pokemon)

                        print(f"Apilado: {pokemon}")

            elif accion == "2":

                try:

                    item = pila_historial.desapilar()

                    print(f"Desapilado: {item}")

                except PilaVaciaError as error:

                    print(f"Error: {error}")

            elif accion != "0":

                print("Opción inválida.")

        # E6: Cola
        elif opcion == "8":

            print("\n========== TURNOS (COLA) ==========")
            print("1. Encolar Pokémon")
            print("2. Desencolar Pokémon")
            print("0. Volver")

            accion = input("> ").strip()

            if accion == "1":

                entrada = input("Ingrese el ID del Pokémon: ").strip()

                if not entrada.isdigit():

                    print("Debe ingresar un ID numérico.")

                else:

                    id_buscado = int(entrada)

                    pokemon = obtener_pokemon_por_id(
                        catalogo,
                        id_buscado
                    )

                    if pokemon is None:

                        print("No se encontró un Pokémon con ese ID.")

                    else:

                        cola_turnos.encolar(pokemon)

                        print(f"Encolado: {pokemon}")

            elif accion == "2":

                try:

                    item = cola_turnos.desencolar()

                    print(f"Turno atendido: {item}")

                except ColaVaciaError as error:

                    print(f"Error: {error}")

            elif accion != "0":

                print("Opción inválida.")

        # E5: Archivos
        elif opcion == "9":

            catalogo = menu_archivos(catalogo)

        else:

            print("Opción inválida.")


# Recuperar el equipo guardado
try:

    equipo = cargar_equipo_binario()

except (ArchivoInvalidoError, OSError) as error:

    raise SystemExit(
        f"No se pudo recuperar el equipo guardado: {error}"
    )


pila_historial = Pila()
cola_turnos = Cola()

menu_principal(equipo, pila_historial, cola_turnos, catalogo)