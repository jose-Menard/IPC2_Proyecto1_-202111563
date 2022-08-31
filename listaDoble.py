from nodo import Nodo
import os

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
    
    def graficar1(self):
        nodoAux = self.raiz
        
        cadena = 'digraph { '  
     
     
        while True:
            if nodoAux.fila is not None:
                cadena += nodoAux.fila.replace(' ', '')
                cadena += nodoAux.columna.replace(' ', '')
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        cadena += "}"
        file = open("./nodo.dot", "w+")
        file.write(cadena)
        file.close()
        os.system('dot -Tpng nodo.dot -o nodo.png')


    def eliminar(self, fila, columna):
        actual=self.raiz
        eliminado=False

        if actual is None:
            eliminado=False
        elif actual.fila==fila and actual.columna==columna:
            self.raiz=actual.siguiente
            self.raiz.anterior=None
            eliminado=True
        elif self.ultimo.fila==fila and self.ultimo.columna==columna:
            self.ultimo=self.ultimo.anterior
            self.ultimo.siguiente=None
            eliminado=True
        else:
            while actual:
                if actual.fila==fila and actual.columna==columna:
                    actual.anterior.siguiente=actual.siguiente
                    actual.siguiente.anterior=actual.anterior
                    eliminado=True
                actual=actual.siguiente
        

        print("se eliminó con exito, creo xd")
            


    

    