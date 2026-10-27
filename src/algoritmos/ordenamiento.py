def ordenar_seleccion(coleccion, clave):
    resultado = list(coleccion)

    for inicio in range(len(resultado)):
        posicion_menor = inicio

        for i in range(inicio + 1, len(resultado)):
            elemento = resultado[i]

            if clave(elemento) < clave(resultado[posicion_menor]):
                posicion_menor = i

        resultado[inicio], resultado[posicion_menor] = resultado[posicion_menor], resultado[inicio]

    return resultado

def ordenar_insercion(coleccion, clave):
    resultado = list(coleccion)

    for i in range(1, len(resultado)):
        actual = resultado[i]
        j = i - 1

        while j >= 0 and clave(resultado[j]) > clave(actual):
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = actual

    return resultado