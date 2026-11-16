# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa |  |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) |  |  |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | `pasa` |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | `pasa` |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | `pasa` |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | `pasa` |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra | `pasa` |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback | `pasa` |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit | `pasa` | Reordena por ID antes de realizar la búsqueda binaria y encuentra a Pikachu. |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar el catálogo en TXT, salir y volver a cargarlo desde el menú | 70 Pokémon | Se recuperan los 70 Pokémon sin perder información | `pasa` | Se comprobó que los datos originales y los recuperados coinciden. |
| P14 | E5 | Guardar el catálogo en binario y modificar el HP de un Pokémon | Bulbasaur, ID 1, HP de 45 a 99 | Se modifica el registro y los demás permanecen sin cambios | `pasa` | Se utilizó actualizar_registro() con seek(). Los otros 69 registros no cambiaron. |
| P15 | E5 | Intentar cargar un archivo binario inválido | Archivo de prueba con cabecera inválida | Se produce ArchivoInvalidoError | `pasa` | Se comprobó la detección de un archivo inválido. |