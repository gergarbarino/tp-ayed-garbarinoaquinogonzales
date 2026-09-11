from catalogo import cargar_catalogo


def main():
    catalogo = cargar_catalogo("docs/data/pokedex.csv")

    while True:
        entrada = input("Ingrese el ID del Pokémon o 'apagar' para salir: ")

        if entrada.lower() == "apagar":
            break

        id_buscado = int(entrada)

        for pokemon in catalogo:
            if pokemon.numero == id_buscado:
                print(pokemon)


if __name__ == "__main__":
    main()
