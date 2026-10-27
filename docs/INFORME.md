# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema:
- Por qué lo eligieron (5–8 líneas):

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | esta_vacia(), tamanio(), buscar(), eliminar(), insertar_al_inicio(), insertar_al_final(), agregar(), iteración mediante __iter__ y __next__ | La lista está formada por nodos enlazados mediante siguiente. La cabeza representa el primer nodo y no se utiliza una list de Python como estructura interna. |
| Pila | apilar(), desapilar(), ver_tope(), esta_vacia() | Mantiene el comportamiento LIFO: el último elemento agregado es el primero en salir. La pila utiliza una ListaEnlazada como estructura interna. |
| Cola | encolar(), desencolar(), ver_frente(), esta_vacia() | Mantiene el comportamiento FIFO: el primer elemento agregado es el primero en salir. La cola utiliza una ListaEnlazada como estructura interna. |

Dónde se usa cada uno en el dominio.

Uso en el dominio:

ListaEnlazada: se utiliza para almacenar el catálogo de Pokémon y los Pokémon del equipo.
Pila: se utiliza como historial para representar la operación de deshacer.
Cola: se utiliza para gestionar los turnos de atención.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Búsqueda lineal | O(n) | O(1) | En el peor caso recorre todos los elementos para encontrar el buscado. |
| Búsqueda binaria | O(log n) | O(1) | En cada iteración descarta la mitad de los elementos restantes. Requiere datos previamente ordenados. |
| Ordenamiento por selección | O(n²) | O(n) | Busca el menor en cada pasada mediante dos ciclos anidados. Crea una copia de la colección. |
| Ordenamiento por inserción | O(n²) | O(n) | En el peor caso desplaza varios elementos por cada inserción. Crea una copia de la colección. |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda lineal | 70 | 0.000002198 |
| Búsqueda lineal | 700 | 0.000021069 |
| Búsqueda binaria | 70 | 0.000000572 |
| Búsqueda binaria | 700 | 0.000000865 |
| Ordenamiento por selección | 70 | 0.000112107 |
| Ordenamiento por selección | 700 | 0.015519662 |
| Ordenamiento por inserción | 70 | 0.000005118 |
| Ordenamiento por inserción | 700 | 0.014697012 |

Análisis de las mediciones (E4)

Para realizar las pruebas se utilizó un catálogo de 70 Pokémon y una colección ampliada de 700 elementos, obtenida mediante la repetición del catálogo original diez veces. Cada algoritmo se ejecutó 10.000 veces y se calculó su tiempo promedio mediante time.perf_counter().

La búsqueda lineal presentó un aumento de tiempo aproximadamente proporcional a la cantidad de elementos. La búsqueda binaria tuvo un crecimiento mucho menor, ya que reduce el espacio de búsqueda en cada iteración. Para esta comparación, el catálogo se ordenó previamente y el tiempo de ordenamiento no se incluyó en la medición de búsqueda.

Los algoritmos de selección e inserción presentaron aumentos de tiempo más importantes. Selección realiza comparaciones mediante ciclos anidados, mientras que inserción depende del orden inicial de los elementos. Las mediciones son consistentes con las características de complejidad estudiadas, aunque los tiempos concretos pueden variar según los datos y la ejecución.

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
