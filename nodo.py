class Nodo:
    def __init__(self, tipo = None, fila = None, columna = None) -> None:
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

        self.siguiente = None
        self.anterior = None