def busqueda_lineal(coleccion, clave, obtener_clave):
    n = len(coleccion)

    for i in range(n):
        elemento = coleccion[i]

        if obtener_clave(elemento) == clave:
            return i

    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):

    izq = 0
    der = len(coleccion_ordenada) - 1

    while izq <= der:
        medio = (izq + der) // 2
        valor_actual = obtener_clave(coleccion_ordenada[medio])

        if valor_actual == clave:
            return medio
        elif valor_actual < clave:
            izq = medio + 1
        else:
            der = medio - 1

    return None