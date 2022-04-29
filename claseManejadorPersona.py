from clasePersona import Persona



class ManejadorPersona:
    __listaP = []
    def __init__ (self):
        self.__listaP = []
    def agregarPersona (self, unaPersona):
        self.__listaP.append(unaPersona)
    def testListaPersona (self):
        #aca creamos las instancias persona, puede ser por archivo csv o desde teclado
        unaPersona = Persona('Roberto', 'Sanchez', 44, 'Informatico')
        otraPersona = Persona ('Julian', 'Fernandez', 33, 'Abogado')
        personaX = Persona ('Alvaro', 'Gimenez', 37, 'Docente')
        PersonaX2 = Persona ("Manuel","Ortega",25,"El mejor docente")
        self.agregarPersona(unaPersona)
        self.agregarPersona(otraPersona)
        print("Aplicamos algunos metodos: ")
        print("Metodo insert")
        self.__listaP.insert (1,personaX)
        print("\nValor de index de Persona Julian: ", self.__listaP.index (otraPersona))
        print("\nEliminamos la Persona que se encuentra en la primera posicion de la lista\n")
        self.__listaP.pop(0)
        print("Usamos el metodo Extend, añadiendo otra vez a Roberto\n")
        self.__listaP.extend([unaPersona, PersonaX2])  #se coloca entre corchetes, pues es iterable
        print("Aplicamos metodo sort para ordenar la lista en base a la edad\n")
        self.__listaP.sort()
    def mostrarListaPersona (self):
        for pers in self.__listaP:
            pers.mostrarPersona()
            print("".center(50, '='))
    

   