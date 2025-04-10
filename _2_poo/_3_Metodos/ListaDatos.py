class ListaDatos:

    def __init__(self, matricula:str, estudiante:str, asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura

if __name__ == '__main__':
    lista =[]
    lista.append(ListaDatos("22240059", "Abril Mendez", "poo"))
    lista.append(ListaDatos("22240057", "Alison Meneses", "poo"))
    lista.append(ListaDatos("22240021", "Dulce Rubi", "poo"))

    for obj in lista:
        print(f"Matricula: {obj.matricula}")
        print(f"Nombre: {obj.estudiante}")
        print(f"Asignatura: {obj.asignatura}")
        print("-------------------------")