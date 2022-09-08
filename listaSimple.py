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
    
    def asignacionMatriz(self, dimensionita, pacientoso, periodito):
            
        if pacientoso is None:
            print(Fore.RED + "El paciente no se encuentra registrado en la lista")
        else:
            for i in range(0, dimensionita):
                for k in range(0,dimensionita):
                
                    nuevoNodo = Nodo(str(0), str(i), str(k))
                    pacientoso.nodo.append(nuevoNodo)

                    
            for i in range(0, periodito):

                print(Fore.GREEN + "--------------------------------Periodo Actual------------------------------\n")

                for f in range(0,pacientoso.contador):
                    pacientoso.nodo.modificar(pacientoso.nodoMalo.nodoActual())
                    pacientoso.nodoMalo.siguiente()
                pacientoso.nodo.recorrer(dimensionita,pacientoso.nodoMalo)
                pacientoso.nodo.print()

                    
                    
                print(Fore.GREEN + "--------------------------------Nuevo Periodo------------------------------\n")
                pacientoso2 = self.buscarPacienteByNombre(pacientoso.nombre)
                pacientoso2.nodo.setear0()
                for f in range(0,pacientoso.contador):
                    pacientoso2.nodo.modificar(pacientoso.nodoMalo.nodoActual())
                    pacientoso2.nodoMalo.siguiente()
            
                pacientoso2.nodo.print()
           
            

                

        

           
            

    
            
           

            
    



 