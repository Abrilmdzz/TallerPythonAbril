class Libro:
    def __init__(self, isbn, titulo, autor):
       self.isbn=isbn
       self.titulo=titulo
       self.autor=autor

if __name__ == '__main__':
    lista=[]
    lista.append(Libro("978-92-95055-02-5", "Harry Potter y el prisionero de azkaban", "J.K Rowlling"))
    lista.append(Libro("989-94-96066-07-6", "The bridgerton", "Julia Quinn"))
    lista.append(Libro("789-86-78072-08-2", "el diario de dorian gray autor", "Oscar Wilde"))

    for obj in lista:
        print(f"Matricula: {obj.isbn}")
        print(f"Nombre: {obj.titulo}")
        print(f"Asignatura: {obj.autor}")
        print("-------------------------")


