from ssl import SSL_ERROR_WANT_X509_LOOKUP
from timeit import repeat
from paciente import Paciente
from colorama import Fore
from nodo import Nodo
import os
from listaDoble import ListaDoble

class ListaSimple:
    def __init__(self) -> None:
        self.raiz = Paciente()
        self.ultimo = Paciente()

    def append(self, nuevoPaciente):
        if self.raiz.nombre is None:
            self.raiz = nuevoPaciente
            self.ultimo = nuevoPaciente
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoPaciente
            self.ultimo = nuevoPaciente
        else:
            self.ultimo.siguiente = nuevoPaciente
            self.ultimo = nuevoPaciente
    
    def print(self):
        nodoAux = self.raiz

        cadena = ''

        while True:
            if nodoAux.nombre is not None:
                cadena += "(" + nodoAux.nombre + " " + nodoAux.edad + " " + nodoAux.periodos +" " + nodoAux.dimension + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)

    def buscarPacienteByNombre(self, nombre):
        nodoAux = self.raiz

        while nodoAux.nombre != nombre:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return nodoAux


    def graficar(self):
        nodoAux = self.raiz
        
        cadena = 'digraph { '  
        while True:
            if nodoAux.nombre is not None:
                cadena += nodoAux.nombre.replace(' ', '')
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
    
    def asignacionMatriz(self, dimensionita, pacientoso):
            
        if pacientoso is None:
            print(Fore.RED + "El paciente no se encuentra registrado en la lista")
        else:
            for i in range(0, dimensionita):
                for k in range(0,dimensionita):
                
                    nuevoNodo = Nodo(str(0), str(k), str(i))
                    pacientoso.nodo.append(nuevoNodo)

                    sexoo=pacientoso.nodo.ultimo.columna

                    print(sexoo)
                    
            print(Fore.GREEN + "Se llenaron los nodos con exito!! \n")

           
            

    
            
           

            
    



 