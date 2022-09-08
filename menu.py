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
    listaMalos= ListaDoble()

    while opcion != '7':
        print(Fore.CYAN + "-----------------MENU---------------")
        print(Fore.CYAN + "1 --- CARGAR DESDE ARCHIVO")
        print(Fore.CYAN + "2 --- IMPRIMIR PACIENTE")
        print(Fore.CYAN + "3 --- MOSTRAR NODOS INFECTADOS POR PACIENTE")
        print(Fore.CYAN + "4 --- LEER REJILLA DEL PACIENTE")
        print(Fore.CYAN + "5 --- GRAFICAR LISTA DE PACIENTES")
        print(Fore.CYAN + "6 --- GRAFICAR REJILLAS")
        print(Fore.CYAN + "7 --- SALIR")

        opcion = input(Fore.YELLOW + "Seleccione una opcion del menu \n")
         
 
        if opcion == '2':
            listaPacientes.print()
        elif opcion == '3':
            nombre = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
            paciente = listaPacientes.buscarPacienteByNombre(nombre)

            if paciente is None:
                print(Fore.RED + "El paciente no se encuentra registrado en la lista")
            else:
                paciente.nodoMalo.print()
        elif opcion == '1':
            nombreArchivo = input(Fore.BLUE + "Ingrese el nombre del archivo XML\n")
            ruta = './' + nombreArchivo
            listaPacientes = cargaArchivo(ruta)
            print(Fore.GREEN + "Se cargo el archivo con exito!!\n")
        elif opcion == '5':
            listaPacientes.graficar()
        elif opcion == '6':
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
                periodito=int(vars(pacientoso).get("periodos"))
                listaPacientes.asignacionMatriz(dimensionita,pacientoso,periodito)

                
                   
            
            
      
def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    pacientes = tree.getroot()
    listaPacientesDesdeXml = ListaSimple()
    for pacienteXml in pacientes:
        nuevoPaciente = Paciente(pacienteXml.attrib['nombre'], pacienteXml.attrib['edad'], pacienteXml.attrib['periodos'], pacienteXml.attrib['dimension'])
        listaPacientesDesdeXml.append(nuevoPaciente)
        for nodoXml in pacienteXml.iter('nodo'):
            nuevoNodo = Nodo(str("1"), nodoXml.attrib['fila'], nodoXml.attrib['columna'])
            nuevoPaciente.nodoMalo.append(nuevoNodo)
            nuevoPaciente.contador=nuevoPaciente.contador+1
            
        
    return listaPacientesDesdeXml



def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    pacientes = tree.getroot()
    listaPacientesDesdeXml = ListaSimple()
    for element in pacientes:
        for m in element.iter("m"):
            print(m.text)
        for periodo in element.iter("periodos"):
            print(periodo.text)

        for datos in element.iter("datospersonales"):
            for dat1 in datos.iter("nombre"):
                print(dat1.text)
            for dat2 in datos.iter("edad"):
                print(dat2.text)
       
            nuevoPaciente = Paciente(dat1.text,dat2.text,periodo.text,m.text)
            listaPacientesDesdeXml.append(nuevoPaciente)
    
    

    
        
        for elementR in element.iter("celda"):

            nuevoNodo=Nodo(str("1"), elementR.attrib['f'], elementR.attrib['c'])
            nuevoPaciente.nodoMalo.append(nuevoNodo)
            nuevoPaciente.contador=nuevoPaciente.contador+1

    
    return listaPacientesDesdeXml
    

            
menu()

