from nodo import Nodo

class ListaDoble:
    def __init__(self) -> None:
        self.raiz = Nodo()
        self.ultimo = Nodo()

    
    def append(self, nuevoNodo):
        if self.raiz.tipo is None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoNodo
            nuevoNodo.anterior = self.raiz
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            nuevoNodo.anterior = self.ultimo
            self.ultimo = nuevoNodo

    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.tipo is not None:
                cadena += "(" + nodoAux.tipo + " " + nodoAux.fila + " " + nodoAux.columna +  ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)     