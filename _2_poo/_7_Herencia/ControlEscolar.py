class ListaDatos:

    def __init__(self, matricula:str, estudiante:str, asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura

class ControlEscolar(ListaDatos):

    def __init__(self):
        self.lista=[]

    def addEstudiante(self, matricula, estudiante, asignatura):
      self.lista.append(ListaDatos(matricula, estudiante, asignatura))

    def show(self):
        for obj in self.lista:
            print(f"Estudiante : {obj.estudiante}")
            print(f"Matricula: {obj.matricula}")
            print(f"Asignatura: {obj.asignatura}")
            print("-------------------------")

if __name__ == '__main__':
    escolar=ControlEscolar()
    escolar.addEstudiante("22240059", "Abril Mendez", "Estructura de datos")
    escolar.addEstudiante("22240059", "Abril Mendez", "poo")
    escolar.addEstudiante("22240059", "Abril Mendez", "Calculo")

    escolar.show()