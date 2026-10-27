import time

from src.catalogo import cargar_catalogo
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion


catalogo = list(cargar_catalogo())

catalogo = catalogo * 10

print("Cantidad de Pokémon:", len(catalogo))

repeticiones = 10000

# BÚSQUEDA LINEAL

inicio = time.perf_counter()

for i in range(repeticiones):
    indice = busqueda_lineal(
        catalogo,
        99999,
        lambda p: p.numero
    )

fin = time.perf_counter()

tiempo_lineal = (fin - inicio) / repeticiones

print("Tiempo promedio búsqueda lineal:", tiempo_lineal)


# BÚSQUEDA BINARIA

catalogo_ordenado = ordenar_insercion(
    catalogo,
    lambda p: p.numero
)

inicio = time.perf_counter()

for i in range(repeticiones):
    indice = busqueda_binaria(
        catalogo_ordenado,
        99999,
        lambda p: p.numero
    )

fin = time.perf_counter()

tiempo_binaria = (fin - inicio) / repeticiones

print("Tiempo promedio búsqueda binaria:", tiempo_binaria)


# ORDENAMIENTO POR SELECCIÓN

inicio = time.perf_counter()

for i in range(repeticiones):
    resultado = ordenar_seleccion(
        catalogo,
        lambda p: p.numero
    )

fin = time.perf_counter()

tiempo_seleccion = (fin - inicio) / repeticiones

print("Tiempo promedio selección:", tiempo_seleccion)


# ORDENAMIENTO POR INSERCIÓN

inicio = time.perf_counter()

for i in range(repeticiones):
    resultado = ordenar_insercion(
        catalogo,
        lambda p: p.numero
    )

fin = time.perf_counter()

tiempo_insercion = (fin - inicio) / repeticiones

print("Tiempo promedio inserción:", tiempo_insercion)