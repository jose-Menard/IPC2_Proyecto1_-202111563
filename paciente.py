from listaDoble import ListaDoble

class Paciente:
    def __init__(self, nombre = None, edad = None, periodos = None, dimension=None) -> None:
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.dimension = dimension
        self.nodo = ListaDoble()
        self.siguiente = None

        
        