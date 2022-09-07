from nodo import Nodo
import os

class ListaDoble:
    def __init__(self) -> None:
        self.raiz = Nodo()
        self.ultimo = Nodo()

    def nodoActual(self):
        return self.raiz


    def siguiente(self):
            if self.raiz.tipo is not None:
                if self.raiz.siguiente is not None:
                    self.raiz = self.raiz.siguiente
                    self.eliminar(self.raiz.anterior.fila,self.raiz.anterior.columna)

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
                    if nodoAux.fila!=nodoAux.siguiente.fila:
                        cadena += "\n"
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)     

    def setear0(self):
        nodoAux = self.raiz
        cadena = ''
    
        while True:
            
            if nodoAux.tipo is not None:
                nodoAux.tipo= "0"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break

    def modificar(self,nodoMalo):
        nodoAux = self.raiz
        cadena = ''
    
        while True:
            
            if nodoAux.tipo is not None:
                if nodoAux.fila == nodoMalo.fila and nodoAux.columna == nodoMalo.columna:
                    
                    nodoAux.tipo= "1"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
    
    def evaluar(self,fila, columna):
        nodoAux = self.raiz
    
        while True:
            if nodoAux.tipo is not None:
                if nodoAux.fila == str(fila) and nodoAux.columna == str(columna):
                    if nodoAux.tipo=="1":
                        return True
                    else:
                        return False
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    return False     
            else:
                return False
    
    def noBorde(self,fila,columna,dimensiosita):
        if int(fila) == -1 or int(columna) == -1 or int(fila)>=dimensiosita or int(columna)>=dimensiosita:
            return 0
        else:
            if self.evaluar(fila,columna) == True:
                return 1
            else:
                return 0

    def recorrer(self,dimensionita,nodoMalo):
        nodoAux = self.raiz

        while True:
            if nodoAux.tipo is not None:
                cont = 0
                fila = nodoAux.fila
                columna = nodoAux.columna
                cont =  cont+ self.noBorde(int(fila)-1,int(columna),dimensionita)
                cont =  cont+ self.noBorde(int(fila)-1,int(columna)+1,dimensionita)                
                cont =  cont+ self.noBorde(int(fila),int(columna)+1,dimensionita)                
                cont =  cont+ self.noBorde(int(fila)+1,int(columna)+1,dimensionita)                
                cont =  cont+ self.noBorde(int(fila)+1,int(columna),dimensionita)                
                cont =  cont+ self.noBorde(int(fila)+1,int(columna)-1,dimensionita)                
                cont =  cont+ self.noBorde(int(fila),int(columna)-1,dimensionita)                
                cont =  cont+ self.noBorde(int(fila)-1,int(columna)-1,dimensionita)
                # otro if para validar si es malo y el contador =3, seguiría siendo malo 
                if cont == 2 or cont ==3:
                    nuevoNodo = Nodo("1",str(fila),str(columna))
                    nodoMalo.append(nuevoNodo)
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                return False

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
