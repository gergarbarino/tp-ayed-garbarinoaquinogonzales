# Pokédex — Trabajo Práctico Integrador

**Universidad Nacional Guillermo Brown (UNAB)**

- Materia: Algoritmos y Estructuras de Datos.
- Ciclo lectivo: 2026.
- Comisión: 1.
- Grupo: 27.
- Tema: Pokédex.
- Lenguaje: Python 3.

## 1. Integrantes

| Nombre | Correo electrónico | GitHub |
| --- | --- | --- |
| Germán Garbarino | galejandro0107@gmail.com | gergarbarino |

Germán Garbarino estuvo a cargo de la continuidad, integración y finalización del proyecto.

## 2. Descripción del proyecto

Este proyecto consiste en una Pokédex desarrollada en Python para la materia Algoritmos y Estructuras de Datos.

El programa permite consultar un catálogo de Pokémon, buscar elementos por número o nombre, ordenar los resultados y administrar un equipo de hasta seis Pokémon.

También incorpora estructuras de datos como listas enlazadas, pilas y colas.

Para representar las evoluciones se utiliza recursividad.

Finalmente, el programa permite guardar y recuperar información mediante archivos de texto y binarios.

La aplicación funciona desde la terminal mediante un menú de opciones.

## 3. Funcionalidades

### Catálogo

- Cargar un catálogo inicial de 70 Pokémon.
- Listar todos los Pokémon disponibles.
- Consultar los detalles de un Pokémon.
- Buscar Pokémon por ID o nombre.
- Ordenar el catálogo por ID o nombre.

### Algoritmos de búsqueda

Se implementaron dos algoritmos:

**Búsqueda lineal**

Recorre los elementos uno por uno hasta encontrar el Pokémon solicitado.

**Búsqueda binaria**

Busca un Pokémon dividiendo progresivamente el espacio de búsqueda.

Para funcionar correctamente, necesita que los datos estén ordenados.

### Algoritmos de ordenamiento

Se implementaron dos algoritmos:

- Ordenamiento por selección.
- Ordenamiento por inserción.

Ambos fueron desarrollados sin utilizar la función `sorted()` de Python.

### Evoluciones recursivas

El programa permite consultar las evoluciones de un Pokémon mediante una función recursiva.

Las relaciones se obtienen del archivo `data/evoluciones.csv`.

Por ejemplo:

Bulbasaur → Ivysaur → Venusaur.

### Equipo Pokémon

El usuario puede:

- Agregar Pokémon al equipo.
- Listar los integrantes.
- Eliminar Pokémon.
- Modificar los puntos de vida (HP).

El equipo tiene un límite de seis Pokémon.

Cuando se intenta superar esa cantidad, el programa utiliza una excepción personalizada.

### Pila e historial

Se implementó una pila utilizando una lista enlazada.

Permite apilar y desapilar Pokémon.

Sigue el comportamiento LIFO: el último elemento en entrar es el primero en salir.

### Cola y turnos

Se implementó una cola utilizando una lista enlazada.

Permite encolar y desencolar Pokémon.

Sigue el comportamiento FIFO: el primer elemento en entrar es el primero en salir.

### Persistencia de archivos

El programa permite:

- Cargar datos desde archivos TXT.
- Guardar datos en archivos TXT.
- Guardar datos en archivos binarios.
- Cargar datos desde archivos binarios.
- Guardar automáticamente los cambios realizados en el equipo.
- Recuperar el equipo al volver a ejecutar el programa.
- Modificar registros binarios mediante `seek()`.

También utiliza excepciones propias para detectar archivos inválidos.

## 4. Requisitos

Para ejecutar el programa se necesita:

- Python 3.10 o superior.
- Una terminal o consola.
- Los archivos del proyecto.

No es necesario instalar bibliotecas externas.

El proyecto utiliza únicamente módulos de la biblioteca estándar de Python.

## 5. Cómo ejecutar el programa

Primero, abrir la carpeta principal del proyecto.

En Windows, se puede utilizar Visual Studio Code y abrir una terminal desde la carpeta donde se encuentra este README.

Ejecutar:

```powershell
py -m src.main
```

También se puede utilizar:

```powershell
python -m src.main
```

Es importante ejecutar el programa desde la carpeta principal del proyecto para que encuentre correctamente los archivos de `data/`.

## 6. Menú principal

Al ejecutar el programa aparece el siguiente menú:

```text
--- Pokédex ---

1. Listar catálogo
2. Ver detalle de un Pokémon
3. Buscar Pokémon
4. Ordenar catálogo
5. Evoluciones (recursividad)
6. Administrar equipo
7. Historial (pila)
8. Turnos (cola)
9. Guardar / cargar archivos
0. Salir
```

El usuario debe ingresar el número correspondiente a la operación que desea realizar.

### Ejemplo de uso

Para consultar las evoluciones de Bulbasaur:

1. Ejecutar el programa.
2. Seleccionar la opción 5.
3. Ingresar el ID 1.

El programa muestra la cadena evolutiva:

```text
#1 Bulbasaur
  #2 Ivysaur
    #3 Venusaur
```

## 7. Estructura del proyecto

```text
tp-integrador/
│
├── data/
│   ├── pokedex.csv
│   ├── pokedex.txt
│   └── evoluciones.csv
│
├── docs/
│   ├── INFORME.md
│   ├── PROTOCOLO_PRUEBAS.md
│   └── DECLARACION_IA.md
│
├── src/
│   ├── main.py
│   ├── pokemon.py
│   ├── catalogo.py
│   ├── equipo.py
│   ├── excepciones.py
│   │
│   ├── algoritmos/
│   │   ├── busqueda.py
│   │   ├── ordenamiento.py
│   │   └── mediciones.py
│   │
│   ├── dominio/
│   │   ├── pokedex.py
│   │   ├── evoluciones.py
│   │   └── listado.py
│   │
│   ├── tads/
│   │   ├── nodo.py
│   │   ├── lista_enlazada.py
│   │   ├── pila.py
│   │   └── cola.py
│   │
│   └── persistencia/
│       ├── texto.py
│       ├── binario.py
│       └── equipo_archivo.py
│
├── README.md
└── GIT.md
```

La estructura muestra los principales archivos utilizados por el programa. La carpeta `data/` también contiene otros archivos CSV proporcionados con el proyecto.

## 8. Estructuras de datos utilizadas

### Lista enlazada

Se utiliza para almacenar el catálogo y los Pokémon del equipo.

Está formada por nodos que contienen un dato y una referencia al siguiente nodo.

### Pila

Se utiliza para almacenar elementos siguiendo el comportamiento LIFO.

### Cola

Se utiliza para administrar turnos siguiendo el comportamiento FIFO.

Estas estructuras fueron implementadas utilizando clases propias.

## 9. Archivos y persistencia

### Archivos CSV y TXT

Los archivos de texto permiten almacenar información de manera legible.

El programa utiliza datos separados por comas y encabezados para identificar los campos.

### Archivos binarios

Para trabajar con archivos binarios se utiliza el módulo `struct`.

Cada archivo contiene una cabecera y registros de longitud fija.

En el formato utilizado para los Pokémon:

- Cabecera: 9 bytes.
- Registro: 58 bytes.

La función `seek()` permite acceder directamente a la posición de un registro para modificarlo.

### Equipo persistente

Los cambios del equipo se almacenan en `data/equipo.bin`.

Esto permite recuperar los Pokémon del equipo después de cerrar y volver a abrir el programa.

El archivo se genera durante el uso del programa.

## 10. Pruebas realizadas

Se realizaron pruebas manuales para verificar:

- Carga y listado de 70 Pokémon.
- Consulta de Pokémon existentes e inexistentes.
- Recursividad de las evoluciones.
- Límite de seis Pokémon en el equipo.
- Pila vacía.
- Cola vacía.
- Búsqueda lineal.
- Búsqueda binaria.
- Ordenamiento por selección.
- Ordenamiento por inserción.
- Guardado y recuperación de archivos TXT.
- Guardado y recuperación de archivos binarios.
- Modificación de registros.
- Detección de archivos binarios inválidos.

Los resultados se encuentran documentados en:

`docs/PROTOCOLO_PRUEBAS.md`

También se realizaron mediciones de rendimiento de los algoritmos de búsqueda y ordenamiento.

Los resultados y el análisis de complejidad se encuentran en:

`docs/INFORME.md`

## 11. Documentación

El proyecto incluye tres documentos principales:

**INFORME.md**

Explica el modelo del programa, los TADs, la recursividad, los algoritmos, su complejidad y la persistencia.

**PROTOCOLO_PRUEBAS.md**

Registra las pruebas manuales, los resultados esperados y los resultados obtenidos.

**DECLARACION_IA.md**

Registra las herramientas de inteligencia artificial utilizadas durante el desarrollo del proyecto.

## 12. Entregas

Las entregas se identifican mediante etiquetas (tags) de Git.

| Entrega | Fecha de vencimiento |
| --- | --- |
| Entrega 1 | 06/09/2026 |
| Entrega 2 | 20/09/2026 |
| Entrega 3 | 04/10/2026 |
| Entrega 4 | 01/11/2026 |
| Entrega 5 | 15/11/2026 |
| Entrega 6 | 22/11/2026 |

Los tags permiten identificar el estado del proyecto correspondiente a cada entrega.

La última entrega se identificará con el tag `entrega-6` una vez finalizadas las verificaciones.

## 13. Defensa oral

La defensa oral del proyecto está prevista para los días 25 y 27 de noviembre de 2026.

Durante la defensa se podrán explicar los algoritmos implementados, las estructuras de datos utilizadas y el funcionamiento general del programa.

## 14. Repositorio

El código fuente se encuentra disponible en GitHub:

https://github.com/gergarbarino/tp-ayed-garbarinoaquinogonzales