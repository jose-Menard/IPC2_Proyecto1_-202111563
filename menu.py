from colorama import Fore
from paciente import Paciente
from listaSimple import ListaSimple
from nodo import Nodo
import xml.etree.ElementTree as ET

def menu():
    opcion = ''
    listaPacientes = ListaSimple()
    while opcion != '8':
        print(Fore.CYAN + "-----------------MENU---------------")
        print(Fore.CYAN + "1 --- CREAR PACIENTE")
        print(Fore.CYAN + "2 --- IMPRIMIR PACIENTE")
        print(Fore.CYAN + "3 --- AGREGAR NODO A PACIENTE")
        print(Fore.CYAN + "4 --- MOSTRAR NODOS POR PACIENTE")
        print(Fore.CYAN + "5 --- CARGAR DESDE ARCHIVO")
        print(Fore.CYAN + "6 --- GRAFICAR LISTA DE PACIENTES")
        print(Fore.CYAN + "8 --- SALIR")

        opcion = input(Fore.YELLOW + "Seleccione una opcion del menu \n")

        if opcion == '1':
            c = input(Fore.BLUE + "Ingrese los datos del paciente en el siguiente formato nombre-edad-periodos\n")
            datos = c.split('-')
            nuevoPaciente = Paciente(datos[0], datos[1], datos[2])
            listaPacientes.append(nuevoPaciente)
            print(Fore.GREEN + "Se registro el paciente con exito!! \n")
        elif opcion == '2':
            listaPacientes.print()

           
        elif opcion == '3':
            nombre = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
            paciente = listaPacientes.buscarPacienteByNombre(nombre)

            if paciente is None:
                print(Fore.RED + "El paciente no se encuentra registrado en la lista")
            else:
                c = input(Fore.BLUE + "Ingrese los datos del nodo en el siguiente formato tipo-fila-columna\n") 
                datos = c.split('-')
                nuevoNodo = Nodo(datos[0], datos[1], datos[2])
                paciente.nodo.append(nuevoNodo)
                print(Fore.GREEN + "Se registro el nodo con exito!! \n")
        elif opcion == '4':
            nombre = input(Fore.BLUE + "Ingresar nombre de paciente: \n")
            paciente = listaPacientes.buscarPacienteByNombre(nombre)

            if paciente is None:
                print(Fore.RED + "El paciente no se encuentra registrado en la lista")
            else:
                paciente.nodo.print()
        elif opcion == '5':
            nombreArchivo = input(Fore.BLUE + "Ingrese el nombre del archivo XML\n")
            ruta = './' + nombreArchivo
            listaPacientes = cargaArchivo(ruta)
            print(Fore.GREEN + "Se cargo el archivo con exito!!\n")
        elif opcion == '6':
            listaPacientes.graficar()


def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    pacientes = tree.getroot()
    listaPacientesDesdeXml = ListaSimple()
    for pacienteXml in pacientes:
        nuevoPaciente = Paciente(pacienteXml.attrib['nombre'], pacienteXml.attrib['edad'], pacienteXml.attrib['periodos'])
        listaPacientesDesdeXml.append(nuevoPaciente)
        for nodoXml in pacienteXml.iter('nodo'):
            nuevoNodo = Nodo(nodoXml.attrib['tipo'], nodoXml.attrib['fila'], nodoXml.attrib['columna'])
            nuevoPaciente.nodo.append(nuevoNodo)
    return listaPacientesDesdeXml



menu()

