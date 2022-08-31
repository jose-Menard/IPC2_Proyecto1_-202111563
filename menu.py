from colorama import Fore
from listaDoble import ListaDoble
from paciente import Paciente
from listaSimple import ListaSimple
from nodo import Nodo
import xml.etree.ElementTree as ET

def menu():
    opcion = ''
    listaPacientes = ListaSimple()
    listaNodos= ListaDoble()
    while opcion != '8':
        print(Fore.CYAN + "-----------------MENU---------------")
        print(Fore.CYAN + "1 --- CARGAR DESDE ARCHIVO")
        print(Fore.CYAN + "2 --- IMPRIMIR PACIENTE")
        print(Fore.CYAN + "3 --- MOSTRAR NODOS POR PACIENTE")
        print(Fore.CYAN + "4 --- RELLENAR REJILLA  DEL PACIENTE")
        print(Fore.CYAN + "5 --- ARREGLAR REJILLA  DEL PACIENTE")
        print(Fore.CYAN + "6 --- GRAFICAR LISTA DE PACIENTES")
        print(Fore.CYAN + "7 --- GRAFICAR REJILLAS")
        print(Fore.CYAN + "8 --- SALIR")

        opcion = input(Fore.YELLOW + "Seleccione una opcion del menu \n")
         
        '''
        if opcion == '1':
            c = input(Fore.BLUE + "Ingrese los datos del paciente en el siguiente formato nombre-edad-periodos-dimension\n")
            datos = c.split('-')
            nuevoPaciente = Paciente(datos[0], datos[1], datos[2], datos[3])
            listaPacientes.append(nuevoPaciente)
            print(Fore.GREEN + "Se registro el paciente con exito!! \n")

        '''
        if opcion == '2':
            listaPacientes.print()

         
 #       elif opcion == '3':
 #          nombre = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
 #           paciente = listaPacientes.buscarPacienteByNombre(nombre)
 #
 #           if paciente is None:
 #              print(Fore.RED + "El paciente no se encuentra registrado en la lista")
 #           else:
 #               c = input(Fore.BLUE + "Ingrese los datos del nodo en el siguiente formato tipo-fila-columna\n") 
 #               datos = c.split('-')
 #               nuevoNodo = Nodo(datos[0], datos[1], datos[2])
 #               paciente.nodo.append(nuevoNodo)
 #               print(Fore.GREEN + "Se registro el nodo con exito!! \n")
               
        elif opcion == '3':
            nombre = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
            paciente = listaPacientes.buscarPacienteByNombre(nombre)

            if paciente is None:
                print(Fore.RED + "El paciente no se encuentra registrado en la lista")
            else:
                paciente.nodo.print()
        elif opcion == '1':
            nombreArchivo = input(Fore.BLUE + "Ingrese el nombre del archivo XML\n")
            ruta = './' + nombreArchivo
            listaPacientes = cargaArchivo(ruta)
            print(Fore.GREEN + "Se cargo el archivo con exito!!\n")
        elif opcion == '6':
            listaPacientes.graficar()
        elif opcion == '7':
            nombrito = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
            pacientito = listaPacientes.buscarPacienteByNombre(nombrito)

            pacientito.nodo.graficar1()
        elif opcion == '4':
            nombroso = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
            pacientoso = listaPacientes.buscarPacienteByNombre(nombroso)

            if pacientoso is None:
                print(Fore.RED + "El paciente no se encuentra registrado en la lista")
            else:
                print("la dimension de la rejilla del paciente es de: "+vars(pacientoso).get("dimension"))
                dimensionita=int(vars(pacientoso).get("dimension"))
                listaPacientes.asignacionMatriz(dimensionita,pacientoso)
        elif opcion == '5':
            nombre = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
            paciente = listaPacientes.buscarPacienteByNombre(nombre)
    
            if paciente is None:
                print(Fore.RED + "El paciente no se encuentra registrado en la lista")
            else:
                
                for i in range (0,5):
                    
                    arregloFilas=[]
                    arregloCol=[]
                    arregloFilas.append(paciente.nodo.raiz.fila)
                    arregloCol.append(paciente.nodo.raiz.columna)

                    print("Las filas contagiadas son: ",arregloFilas)
                    print("Las columnas contagiadas son: " ,arregloCol)

                print(paciente.nodo.raiz.tipo)
                while paciente.nodo.raiz.tipo !="0":
                    filosa=paciente.nodo.raiz.fila
                    columnosa=paciente.nodo.raiz.columna
                    paciente.nodo.eliminar(filosa, columnosa)

                #filosa = input(Fore.BLUE + "Ingrese la fila del Nodo a eliminar: \n")
                #columnosa = input(Fore.BLUE + "Ingrese la columna del Nodo a eliminar: \n")
                #paciente.nodo.eliminar(filosa, columnosa)
                
                
                   
            
            


def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    pacientes = tree.getroot()
    listaPacientesDesdeXml = ListaSimple()
    for pacienteXml in pacientes:
        nuevoPaciente = Paciente(pacienteXml.attrib['nombre'], pacienteXml.attrib['edad'], pacienteXml.attrib['periodos'], pacienteXml.attrib['dimension'])
        listaPacientesDesdeXml.append(nuevoPaciente)
        for nodoXml in pacienteXml.iter('nodo'):
            nuevoNodo = Nodo(nodoXml.attrib['tipo'], nodoXml.attrib['fila'], nodoXml.attrib['columna'])
            nuevoPaciente.nodo.append(nuevoNodo)
            
            columnosa=nuevoNodo.columna
            filosa=nuevoNodo.fila
    
            print("la columna es:" +columnosa)
            print("la fila es es:" +filosa)
    return listaPacientesDesdeXml



menu()

