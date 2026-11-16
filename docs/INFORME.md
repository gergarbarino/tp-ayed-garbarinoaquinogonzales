# Informe del Trabajo Práctico Integrador

## 1. Grupo y tema

- Universidad: Universidad Nacional Guillermo Brown (UNAB).
- Materia: Algoritmos y Estructuras de Datos.
- Comisión: 1.
- Grupo: 27.
- Tema: Pokédex — Sistema de gestión de Pokémon.
- Integrante responsable de la finalización: Germán Garbarino.

### ¿Por qué elegimos este tema?

Elegimos desarrollar una Pokédex porque permite trabajar con datos conocidos y fáciles de identificar.

Cada Pokémon tiene características como nombre, número, tipos, puntos de vida, ataque, defensa y velocidad.

Este tema permite aplicar los contenidos de Algoritmos y Estructuras de Datos a un programa concreto.

Podemos utilizar búsquedas para encontrar Pokémon, ordenamientos para organizar el catálogo y listas enlazadas para almacenar elementos.

También podemos implementar pilas, colas y recursividad mediante operaciones relacionadas con los Pokémon.

Finalmente, el proyecto permite trabajar con archivos para guardar y recuperar información entre distintas ejecuciones del programa.


## 2. Modelo

### ¿Qué representa un ítem del catálogo?

Un ítem del catálogo representa un Pokémon.

Cada Pokémon es un objeto de la clase `Pokemon` y contiene los siguientes atributos:

- `numero`: número de identificación del Pokémon.
- `nombre`: nombre del Pokémon.
- `tipo1`: tipo principal.
- `tipo2`: tipo secundario.
- `hp`: puntos de vida.
- `ataque`: puntos de ataque.
- `defensa`: puntos de defensa.
- `velocidad`: velocidad del Pokémon.
- `generation`: generación a la que pertenece.

Por ejemplo, Bulbasaur tiene el número 1, es de tipo Planta/Veneno y tiene 45 puntos de vida en el catálogo original.

### Datos mutables e inmutables

En nuestra aplicación, el HP es un dato mutable porque puede modificarse desde el menú del equipo.

El número de identificación, el nombre, los tipos y la generación se mantienen sin cambios durante las operaciones normales del programa.

Esto no significa que Python impida modificarlos, sino que nuestra aplicación no ofrece operaciones para hacerlo.

También puede modificarse el contenido del equipo al agregar o eliminar Pokémon.

### Relación entre las clases y estructuras

**Pokemon**

Representa un Pokémon individual y almacena sus características.

**ListaEnlazada**

Almacena elementos mediante nodos conectados entre sí.

Cada nodo contiene un dato y una referencia al siguiente nodo.

**Catálogo**

Contiene los Pokémon disponibles para consultar, buscar y ordenar.

El catálogo inicial se carga desde el archivo `data/pokedex.csv` y utiliza una `ListaEnlazada`.

**Equipo**

Representa el equipo de Pokémon del usuario.

Utiliza una `ListaEnlazada` y tiene una capacidad máxima de seis Pokémon.

**Pila**

Permite almacenar y retirar Pokémon siguiendo el comportamiento LIFO: el último en entrar es el primero en salir.

Internamente utiliza una `ListaEnlazada`.

**Cola**

Permite administrar turnos siguiendo el comportamiento FIFO: el primero en entrar es el primero en salir.

Internamente utiliza una `ListaEnlazada`.

### Funcionamiento general

Al iniciar el programa, se carga el catálogo desde el archivo CSV.

El usuario puede listar Pokémon, consultar sus características, realizar búsquedas y ordenar los resultados.

También puede administrar un equipo de hasta seis Pokémon.

La pila permite agregar y retirar Pokémon siguiendo el orden LIFO.

La cola permite gestionar turnos siguiendo el orden FIFO.

Por último, el programa permite guardar y recuperar información mediante archivos de texto y binarios.


## 3. Recursión (E2)

### Función

Se implementó la función `mostrar_evoluciones_recursivas()` en el archivo `src/dominio/evoluciones.py`.

Esta función permite recorrer y mostrar las evoluciones de un Pokémon utilizando recursividad.

Las relaciones entre Pokémon se obtienen del archivo `data/evoluciones.csv`, que contiene los campos `origen_id` y `destino_id`.

### Caso base

El caso base ocurre cuando el Pokémon actual no tiene ninguna evolución registrada.

Se utiliza la condición:

```python
if id_pokemon not in relaciones:
    return
```

Cuando se cumple esta condición, la función termina sin realizar nuevas llamadas recursivas.

Por ejemplo, Venusaur (ID 3) no tiene más evoluciones registradas, por lo que representa el caso base.

### Caso recursivo

El caso recursivo ocurre cuando el Pokémon tiene una o más evoluciones registradas.

La función recorre los ID de sus evoluciones y se llama nuevamente a sí misma:

```python
for siguiente_id in relaciones[id_pokemon]:

    mostrar_evoluciones_recursivas(
        siguiente_id,
        catalogo,
        relaciones,
        nivel + 1
    )
```

En cada llamada se utiliza el ID del siguiente Pokémon.

El parámetro `nivel` aumenta en una unidad para mostrar visualmente la profundidad de la evolución.

### Traza de un ejemplo real del dataset

Se utilizó la cadena evolutiva de Bulbasaur:

Bulbasaur (ID 1) → Ivysaur (ID 2) → Venusaur (ID 3).

| Llamada | Pokémon | Acción |
| --- | --- | --- |
| 1 | Bulbasaur (ID 1) | Muestra Bulbasaur y llama a la función con el ID 2. |
| 2 | Ivysaur (ID 2) | Muestra Ivysaur y llama a la función con el ID 3. |
| 3 | Venusaur (ID 3) | Muestra Venusaur y encuentra el caso base. |
| Retorno | Venusaur → Ivysaur → Bulbasaur | Las llamadas finalizan en orden inverso. |

Salida obtenida:

```text
#1 Bulbasaur
  #2 Ivysaur
    #3 Venusaur
```

También se probó la función directamente con Venusaur (ID 3).

En ese caso solamente se mostró Venusaur, ya que no tiene evoluciones registradas.

### Conclusión

La recursividad permite resolver el recorrido de las evoluciones dividiendo el problema en llamadas más pequeñas de la misma función.

Cada llamada procesa un Pokémon y continúa con sus evoluciones hasta encontrar el caso base.


## 4. Tipos Abstractos de Datos — TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | `esta_vacia()`, `tamanio()`, `buscar()`, `eliminar()`, `insertar_al_inicio()`, `insertar_al_final()`, `agregar()`, `__iter__()` y `__next__()` | La lista está formada por nodos enlazados mediante `siguiente`. La cabeza representa el primer nodo y no se utiliza una lista de Python como estructura interna. |
| Pila | `apilar()`, `desapilar()`, `ver_tope()`, `esta_vacia()` | Mantiene el comportamiento LIFO: el último elemento agregado es el primero en salir. |
| Cola | `encolar()`, `desencolar()`, `ver_frente()`, `esta_vacia()` | Mantiene el comportamiento FIFO: el primer elemento agregado es el primero en salir. |

### Uso de cada TAD en el programa

**ListaEnlazada**

Se utiliza para almacenar el catálogo de Pokémon y los Pokémon que forman parte del equipo.

Permite recorrer sus elementos mediante un iterador propio.

**Pila**

Se utiliza en la opción Historial del menú.

Permite apilar y desapilar Pokémon siguiendo el comportamiento LIFO.

Por ejemplo, si se apilan Bulbasaur, Pikachu y Charmander, el primero en salir será Charmander.

**Cola**

Se utiliza para gestionar los turnos de atención.

Permite encolar y desencolar Pokémon siguiendo el comportamiento FIFO.

Por ejemplo, si se encolan Bulbasaur, Pikachu y Charmander, el primero en salir será Bulbasaur.

### Excepciones propias

Se utilizan excepciones personalizadas para controlar situaciones especiales.

- `ColeccionLlenaError`: cuando se intenta agregar un séptimo Pokémon al equipo.
- `PilaVaciaError`: cuando se intenta desapilar una pila vacía.
- `ColaVaciaError`: cuando se intenta desencolar una cola vacía.

Estas excepciones permiten mostrar mensajes claros sin finalizar inesperadamente el programa.


## 5. Complejidad (E4)

### Complejidad de los algoritmos

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Búsqueda lineal | O(n) | O(1) | En el peor caso recorre todos los elementos para encontrar el buscado. |
| Búsqueda binaria | O(log n) | O(1) | En cada iteración descarta la mitad de los elementos restantes. Requiere datos previamente ordenados. |
| Ordenamiento por selección | O(n²) | O(n) | Busca el menor en cada pasada mediante dos ciclos anidados. Crea una copia de la colección. |
| Ordenamiento por inserción | O(n²) | O(n) | En el peor caso desplaza varios elementos por cada inserción. Crea una copia de la colección. |

### Mediciones con time.perf_counter()

| Operación | n | Segundos |
| --- | --- | --- |
| Búsqueda lineal | 70 | 0.000002198 |
| Búsqueda lineal | 700 | 0.000021069 |
| Búsqueda binaria | 70 | 0.000000572 |
| Búsqueda binaria | 700 | 0.000000865 |
| Ordenamiento por selección | 70 | 0.000112107 |
| Ordenamiento por selección | 700 | 0.015519662 |
| Ordenamiento por inserción | 70 | 0.000005118 |
| Ordenamiento por inserción | 700 | 0.014697012 |

### Análisis de las mediciones

Para realizar las pruebas se utilizó un catálogo de 70 Pokémon y una colección ampliada de 700 elementos, obtenida mediante la repetición del catálogo original diez veces.

Cada algoritmo se ejecutó 10.000 veces y se calculó su tiempo promedio mediante `time.perf_counter()`.

La búsqueda lineal presentó un aumento de tiempo aproximadamente proporcional a la cantidad de elementos.

La búsqueda binaria tuvo un crecimiento mucho menor, ya que reduce el espacio de búsqueda en cada iteración.

Para esta comparación, el catálogo se ordenó previamente y el tiempo de ordenamiento no se incluyó en la medición de búsqueda.

Los algoritmos de selección e inserción presentaron aumentos de tiempo más importantes.

Selección realiza comparaciones mediante ciclos anidados, mientras que inserción depende del orden inicial de los elementos.

Las mediciones son consistentes con las características de complejidad estudiadas, aunque los tiempos concretos pueden variar según los datos y la ejecución.

### Consideraciones

Los tiempos de complejidad indicados corresponden a los algoritmos de búsqueda y ordenamiento.

Como el catálogo utiliza una `ListaEnlazada`, algunas operaciones convierten sus elementos a una lista de Python antes de realizar la búsqueda o el ordenamiento.

Esta conversión necesita recorrer los elementos y tiene un costo adicional O(n).

Además, la búsqueda binaria necesita que los elementos estén ordenados previamente.

Por lo tanto, si es necesario ordenar el catálogo antes de buscar, también debe considerarse el tiempo del ordenamiento.


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

### Cabecera

Formato: `<4s 1s I`

| Campo | Tipo | Tamaño | Descripción |
| --- | --- | --- | --- |
| Magia | 4s | 4 bytes | Identificador `AYED`. |
| Tema | 1s | 1 byte | Identificador `P` (Pokédex). |
| Cantidad | I | 4 bytes | Cantidad de registros. |

Tamaño total de la cabecera: **9 bytes**.

### Registro de Pokémon

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

```python
desplazamiento = 9 + posicion * 58
```

Donde:

- 9 representa el tamaño de la cabecera.
- `posicion` es el índice del registro.
- 58 representa el tamaño de cada registro.

La función `seek()` mueve el cursor del archivo hasta la posición calculada.

Luego se escribe el registro actualizado sin modificar los demás.

Se probó modificando el HP de Bulbasaur de 45 a 99. Los otros 69 registros del catálogo utilizado en esa prueba permanecieron sin cambios.

### ABM persistente del equipo

Se implementaron operaciones de Alta, Baja y Modificación sobre el equipo Pokémon.

**Alta**

Permite agregar un Pokémon y guardar el equipo en `data/equipo.bin`.

**Baja**

Permite eliminar un Pokémon del equipo y guardar el cambio.

**Modificación**

Permite cambiar el HP de un Pokémon utilizando `actualizar_registro()` y `seek()`.

En las operaciones de alta y baja desde el menú se guarda nuevamente el equipo completo.

La modificación del HP se realiza directamente sobre el registro binario correspondiente.

Cuando se inicia el programa, el equipo se recupera automáticamente desde el archivo binario.

Se comprobó que los cambios se conservan después de cerrar y volver a ejecutar la Pokédex.

### Validación de archivos

Se incorporaron controles para detectar archivos inexistentes o inválidos.

En los archivos binarios se verifica la cabecera, la cantidad de registros y el tamaño de los datos.

Cuando se detecta un archivo inválido, se utiliza la excepción `ArchivoInvalidoError`.

Se realizó una prueba intentando cargar un archivo con una identificación incorrecta.

El programa detectó el problema y mostró el mensaje:

```text
La identificación del archivo es incorrecta.
```

Esto permite evitar que el programa interprete como válido un archivo con un formato incorrecto.


## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
| Germán Garbarino | Continuidad y finalización del proyecto. Implementación e integración de búsquedas, ordenamientos, recursividad, persistencia de archivos, operaciones del equipo, menú principal, pruebas y documentación. | Funcionamiento general de la Pokédex, clases, TADs, búsquedas, ordenamientos, recursividad, persistencia y complejidad. |

### Observaciones

Aunque el proyecto se inició como un trabajo grupal, durante su desarrollo se interrumpió la participación de otros integrantes.

Germán Garbarino continuó con la implementación, integración, verificación y documentación necesarias para completar el trabajo.

Se realizaron pruebas de regresión sobre las funcionalidades de las entregas anteriores para comprobar que continuaran funcionando.


## 8. Pruebas de funcionamiento

Las pruebas manuales se encuentran documentadas en `docs/PROTOCOLO_PRUEBAS.md`.

Se comprobaron las siguientes funcionalidades:

- Carga y listado del catálogo de 70 Pokémon.
- Consulta de un Pokémon existente.
- Consulta de un Pokémon inexistente.
- Recorrido recursivo de evoluciones.
- Control del límite de seis Pokémon en el equipo.
- Funcionamiento de la pila y la cola.
- Búsqueda lineal por ID y nombre.
- Búsqueda binaria sobre datos ordenados.
- Ordenamiento por selección.
- Ordenamiento por inserción.
- Guardado y recuperación de archivos de texto.
- Guardado y recuperación de archivos binarios.
- Modificación de registros mediante `seek()`.
- Detección de archivos binarios inválidos.
- Persistencia de las operaciones del equipo.

Las pruebas P01 a P15 se ejecutaron satisfactoriamente durante la verificación de la Entrega 6.


## 9. Conclusión

El desarrollo de la Pokédex permitió aplicar los principales contenidos trabajados durante la materia Algoritmos y Estructuras de Datos.

Se utilizaron clases, objetos, listas enlazadas, pilas, colas, recursividad, algoritmos de búsqueda y ordenamiento.

También se incorporó persistencia mediante archivos de texto y binarios, incluyendo operaciones de modificación por acceso directo.

Las pruebas realizadas permitieron verificar el funcionamiento de las distintas partes del programa y comprobar que las funcionalidades de entregas anteriores continuaran funcionando.

El proyecto permitió relacionar los conceptos teóricos de la materia con una aplicación que puede ejecutarse y utilizarse desde un menú.