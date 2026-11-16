def listar_catalogo(catalogo):

    print("\n========== CATÁLOGO POKÉMON ==========")

    cantidad = 0

    for pokemon in catalogo:

        print(pokemon)

        cantidad += 1

    if cantidad == 0:

        print("El catálogo está vacío.")

    else:

        print(f"\nTotal de Pokémon: {cantidad}")


def ver_detalle(catalogo, id_buscado):

    for pokemon in catalogo:

        if pokemon.numero == id_buscado:

            print("\n========== DETALLE POKÉMON ==========")

            print(f"ID: {pokemon.numero}")
            print(f"Nombre: {pokemon.nombre}")
            print(f"Tipo 1: {pokemon.tipo1}")
            print(f"Tipo 2: {pokemon.tipo2 or 'Ninguno'}")
            print(f"HP: {pokemon.hp}")
            print(f"Ataque: {pokemon.ataque}")
            print(f"Defensa: {pokemon.defensa}")
            print(f"Velocidad: {pokemon.velocidad}")
            print(f"Generación: {pokemon.generation}")

            return True

    print("No se encontró un Pokémon con ese ID.")

    return False