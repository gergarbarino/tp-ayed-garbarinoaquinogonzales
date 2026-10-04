from src.catalogo import cargar_catalogo
from src.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

catalogo = cargar_catalogo()


def buscar_pokemon(catalogo):
    entrada = input("Ingrese el ID del Pokémon: ")

    if entrada.lower() == "apagar":
        return False

    id_buscado = int(entrada)

    pokemon_encontrado = False

    for pokemon in catalogo:
        if id_buscado == pokemon.numero:
            print(pokemon)
            pokemon_encontrado = True
            break

    if pokemon_encontrado == False:
        print("No se encontró un Pokémon con ese ID.")

    return True


def menu_coleccion(equipo, pila_historial, cola_turnos, catalogo):

    while True:
        print("\n--- Colección Principal ---")
        print("1. Agregar al equipo")
        print("2. Listar equipo")
        print("3. Deshacer (pila)")
        print("4. Siguiente turno (cola)")
        print("5. Buscar Pokémon")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            break

        elif opcion == "1":
            entrada = input("Ingrese el ID del Pokémon: ").strip()
            id_buscado = int(entrada)

            pokemon_encontrado = None

            for pokemon in catalogo:
                if pokemon.numero == id_buscado:
                    pokemon_encontrado = pokemon
                    break

            if pokemon_encontrado is None:
                print("No se encontró un Pokémon con ese ID.")
            else:
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


equipo = Equipo()
pila_historial = Pila()
cola_turnos = Cola()

menu_coleccion(equipo, pila_historial, cola_turnos, catalogo)