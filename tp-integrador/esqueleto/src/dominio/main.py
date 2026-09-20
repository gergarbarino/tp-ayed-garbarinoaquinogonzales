from catalogo import cargar_catalogo
from evoluciones import cargar_evoluciones


def main():
    catalogo = cargar_catalogo("docs/data/pokedex.csv")
    evoluciones = cargar_evoluciones("docs/data/evoluciones.csv")

    while True:
        entrada = input("Ingrese el ID del Pokémon o 'apagar' para salir: ")

        if entrada.lower() == "apagar":
            break

        id_buscado = int(entrada)

        pokemon_encontrado = False

        for pokemon in catalogo:
            if pokemon.numero == id_buscado:
                print(pokemon)
                pokemon_encontrado = True

                id_actual = pokemon.numero

                while True:
                    evolucion_encontrada = False

                    for evolucion in evoluciones:
                        if evolucion[0] == id_actual:
                            id_destino = evolucion[1]

                            for pokemon_evolucion in catalogo:
                                if pokemon_evolucion.numero == id_destino:
                                    print("Evoluciona a:", pokemon_evolucion)
                                    id_actual = pokemon_evolucion.numero
                                    evolucion_encontrada = True
                                    break

                            break

                    if not evolucion_encontrada:
                        break

                break

        if not pokemon_encontrado:
            print("No se encontró un Pokémon con ese ID.")


if __name__ == "__main__":
    main()