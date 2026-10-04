from src.tads.nodo import Nodo


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def tamanio(self):
        cantidad = 0
        actual = self.cabeza

        while actual is not None:
            cantidad += 1
            actual = actual.siguiente

        return cantidad

    def buscar(self, dato):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == dato:
                return actual.dato

            actual = actual.siguiente

        return None

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza

        while actual.siguiente is not None and actual.siguiente.dato != dato:
            actual = actual.siguiente

        if actual.siguiente is not None:
            actual.siguiente = actual.siguiente.siguiente

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def agregar(self, dato):
        self.insertar_al_final(dato)

    def __iter__(self):
        return self._Iterador(self.cabeza)

    class _Iterador:

        def __init__(self, cabeza):
            self._actual = cabeza

        def __iter__(self):
            return self

        def __next__(self):
            if self._actual is None:
                raise StopIteration

            dato = self._actual.dato
            self._actual = self._actual.siguiente
            return dato
