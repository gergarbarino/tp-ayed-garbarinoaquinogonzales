# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Ejecutar el programa y seleccionar la opción 1 | Catálogo de 70 Pokémon | Muestra el catálogo completo sin errores | `pasa` | Se mostraron los 70 Pokémon y el programa regresó al menú. |
| P02 | E1 | Seleccionar la opción 2 e ingresar un ID inexistente | ID = -1 | Informa que el Pokémon no existe y permite continuar | `pasa` | Se mostró el mensaje correspondiente y el menú siguió funcionando. |
| P03 | E2 | Elegir la opción 5 e ingresar el ID 1 | Bulbasaur (ID 1) | Muestra Bulbasaur, Ivysaur y Venusaur en orden | `pasa` | Se comprobó el recorrido recursivo de una cadena de tres Pokémon. |
| P04 | E2 | Elegir la opción 5 e ingresar el ID 3 | Venusaur (ID 3) | Muestra únicamente Venusaur y termina la recursión | `pasa` | Se comprobó que la función alcanza correctamente el caso base. |
| P05 | E3 | Completar el equipo con seis Pokémon e intentar agregar un séptimo desde la opción 6 | Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard y Squirtle | El séptimo Pokémon no se agrega y aparece ColeccionLlenaError | `pasa` | Se comprobó el límite de seis Pokémon y que el programa continúa funcionando después del error. |
| P06 | E3 | Iniciar el programa, elegir la opción 7 y después la opción 2 sin haber apilado elementos | Pila vacía | Muestra el mensaje de PilaVaciaError y el menú continúa | `pasa` | Se mostró "La pila está vacía" y el programa siguió funcionando. |
| P07 | E3 | Iniciar el programa, elegir la opción 8 y después la opción 2 sin haber encolado elementos | Cola vacía | Muestra el mensaje de ColaVaciaError y el menú continúa | `pasa` | Se mostró "La cola está vacía" y el programa siguió funcionando. |
| P08 | E3 | Agregar Pokémon al equipo y listarlos utilizando la opción 6 | Pokémon con ID del 1 al 6 | Los Pokémon aparecen en el mismo orden en que fueron agregados | `pasa` | Se comprobó que el iterador de ListaEnlazada respeta el orden de inserción. |
| P09 | E4 | Elegir la opción 3, búsqueda lineal y búsqueda por nombre | Pikachu | Encuentra al Pokémon existente | `pasa` | Se encontró correctamente a Pikachu (ID 25) mediante búsqueda lineal. |
| P10 | E4 | Elegir la opción 3, búsqueda lineal y búsqueda por nombre | PokemonInexistente | Informa que no se encontró el Pokémon y el menú continúa | `pasa` | Se mostró el mensaje correspondiente sin errores. |
| P11 | E4 | Ordenar el catálogo por nombre y después realizar una búsqueda binaria por ID | Gengar (ID 94) | Ordena los datos por ID antes de buscar y encuentra al Pokémon correctamente | `pasa` | Se comprobó que la búsqueda binaria utiliza una copia ordenada por el criterio de búsqueda. |
| P12 | E4 | Ordenar por nombre mediante inserción, listar el catálogo y después ordenar por ID mediante selección | Catálogo de 70 Pokémon | El catálogo cambia de orden según el criterio seleccionado | `pasa` | Se comprobó el orden alfabético por nombre y posteriormente el orden numérico ascendente por ID. |
| P13 | E5 | Guardar TXT, salir, reiniciar, cargar TXT y listar | 70 Pokémon | Se conservan los datos | `pasa` | Se verificó que se cargan y listan los 70 Pokémon. |
| P14 | E5 | Modificar HP de Bulbasaur, reiniciar y consultar | ID 1, HP 45 a 99 | El cambio persiste en binario | `pasa` | Probado desde el menú del equipo. Se restauró el HP original. |
| P15 | E5 | Intentar cargar un archivo binario inválido | Archivo con identificación incorrecta | Se lanza ArchivoInvalidoError | `pasa` | Se detectó el archivo inválido sin modificar los archivos originales. |
| P16 | E5 | Agregar un Pokémon, salir y volver a iniciar el programa | Pikachu (ID 25) | El Pokémon permanece guardado en el equipo | `pasa` | Se comprobó la persistencia del alta durante E5. |
| P17 | E5 | Eliminar un Pokémon, salir y volver a iniciar el programa | Pikachu (ID 25) | El Pokémon eliminado no vuelve a aparecer en el equipo | `pasa` | Se comprobó la persistencia de la baja durante E5. |
| P18 | E5 | Modificar el HP de un Pokémon, salir y volver a iniciar el programa | Bulbasaur (ID 1), HP de 99 a 45 | El nuevo HP permanece guardado | `pasa` | Se comprobó la modificación mediante seek() desde el menú durante E5. |