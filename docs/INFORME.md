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

### Archivos de texto

Se implementaron funciones para leer y escribir archivos de texto en `src/persistencia/texto.py`.

El archivo `data/pokedex.txt` contiene los datos de los Pokémon separados por comas, con un encabezado que identifica los campos.

La función `cargar_texto()` lee los registros y devuelve una lista de diccionarios.

La función `guardar_texto()` permite guardar los datos nuevamente.

Se comprobó que los 70 Pokémon pueden guardarse y recuperarse sin perder información.

### Archivos binarios

Se implementaron funciones de persistencia binaria utilizando el módulo `struct` de Python.

El archivo binario contiene una cabecera y registros de longitud fija.

**Cabecera:**

Formato: `<4s 1s I`

| Campo | Tipo | Tamaño | Descripción |
| --- | --- | --- | --- |
| Magia | 4s | 4 bytes | Identificador `AYED` |
| Tema | 1s | 1 byte | Identificador `P` (Pokédex) |
| Cantidad | I | 4 bytes | Cantidad de registros |

Tamaño total de la cabecera: **9 bytes**.

**Registro de Pokémon:**

Formato: `<I 20s 12s 12s 5H`

| Campo | Tipo | Tamaño |
| --- | --- | --- |
| ID | I | 4 bytes |
| Nombre | 20s | 20 bytes |
| Tipo 1 | 12s | 12 bytes |
| Tipo 2 | 12s | 12 bytes |
| HP | H | 2 bytes |
| Ataque | H | 2 bytes |
| Defensa | H | 2 bytes |
| Velocidad | H | 2 bytes |
| Generación | H | 2 bytes |

Tamaño de cada registro: **58 bytes**.

Para 70 Pokémon, el tamaño total del archivo es:

9 + (70 × 58) = **4069 bytes**.

### Actualización mediante seek()

Se implementó la función `actualizar_registro()` para modificar un registro binario por su posición.

La posición comienza desde 0.

Para calcular dónde comienza un registro se utiliza:

`desplazamiento = 9 + posicion * 58`

Donde:

- 9 representa el tamaño de la cabecera.
- posicion es el índice del registro.
- 58 representa el tamaño de cada registro.

La función `seek()` mueve el cursor del archivo hasta la posición calculada.

Luego se escribe el registro actualizado sin modificar los demás.

Se probó modificando el HP de Bulbasaur de 45 a 99. Los otros 69 registros permanecieron sin cambios.

### ABM persistente del equipo

Se implementaron operaciones de Alta, Baja y Modificación sobre el equipo Pokémon.

- **Alta:** permite agregar un Pokémon y guardar el equipo en `data/equipo.bin`.
- **Baja:** permite eliminar un Pokémon del equipo y guardar el cambio.
- **Modificación:** permite cambiar el HP de un Pokémon utilizando `actualizar_registro()` y `seek()`.

En las operaciones de alta y baja desde el menú se guarda nuevamente el equipo completo. La modificación del HP se realiza directamente sobre el registro binario correspondiente.

Cuando se inicia el programa, el equipo se recupera automáticamente desde el archivo binario.

Se comprobó que los cambios se conservan después de cerrar y volver a ejecutar la Pokédex.

### Validación de archivos

Se incorporaron controles para detectar archivos inexistentes o inválidos.

En los archivos binarios se verifica la cabecera, la cantidad de registros y el tamaño de los datos.

Cuando se detecta un archivo inválido, se utiliza la excepción `ArchivoInvalidoError`.

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
