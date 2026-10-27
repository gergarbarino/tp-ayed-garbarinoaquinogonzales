from src.catalogo import cargar_catalogo
from src.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

catalogo = cargar_catalogo()


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
        indice = busqueda_binaria(datos, clave, obtener_clave)
    else:
        indice = busqueda_lineal(datos, clave, obtener_clave)

    if indice is not None:
        pokemon = datos[indice]
        print(f"¡Encontrado!: {pokemon}")
    else:
        print("No se encontró un Pokémon con ese dato.")

    return True


def menu_coleccion(equipo, pila_historial, cola_turnos, catalogo):

    while True:
        print("\n--- Colección Principal ---")
        print("1. Agregar al equipo")
        print("2. Listar equipo")
        print("3. Deshacer (pila)")
        print("4. Siguiente turno (cola)")
        print("5. Buscar Pokémon")
        print("6. Ordenar catálogo")
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
                    datos, id_buscado, lambda p: p.numero
                )

                if indice is None:
                    print("No se encontró un Pokémon con ese ID.")
                else:
                    pokemon_encontrado = datos[indice]

                    try:
                        equipo.agregar(pokemon_encontrado)
                        print(f"Agregado: {pokemon_encontrado}")
                    except ColeccionLlenaError as e:
                        print(f"Error: {e}")

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
                catalogo = ordenar_seleccion(catalogo, lambda p: p.numero)
                print("Catálogo ordenado por ID (Selección).")
            elif metodo == "2":
                catalogo = ordenar_insercion(catalogo, lambda p: p.nombre)
                print("Catálogo ordenado por Nombre (Inserción).")


equipo = Equipo()
pila_historial = Pila()
cola_turnos = Cola()

menu_coleccion(equipo, pila_historial, cola_turnos, catalogo)