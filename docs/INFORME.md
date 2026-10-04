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
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
