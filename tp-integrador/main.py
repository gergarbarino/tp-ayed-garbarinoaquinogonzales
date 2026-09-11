import csv


def cargar_pokemon(archivo):
    pokemon = []

    with open(archivo, "r", encoding="utf-8") as archivo_csv:
        lector = csv.DictReader(archivo_csv)

        for fila in lector:
            pokemon.append(fila)

    return pokemon


def cargar_evoluciones(archivo):
    evoluciones = []

    with open(archivo, "r", encoding="utf-8") as archivo_csv:
        lector = csv.DictReader(archivo_csv)

        for fila in lector:
            evoluciones.append(fila)

    return evoluciones


def listar_pokemon(pokemon):
    print("\n========== POKÉDEX ==========\n")

    for p in pokemon:
        print(
            f'{p["id"]} - {p["nombre"]} '
            f'({p["tipo1"]}/{p["tipo2"]})'
        )


def mostrar_menu():
    print("\n========== POKÉDEX ==========")
    print("1. Listar Pokémon")
    print("2. Salir")


def main():
    pokemon = cargar_pokemon("pokemon.csv")
    evoluciones = cargar_evoluciones("evoluciones.csv")

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_pokemon(pokemon)

        elif opcion == "2":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
