if __name__ == '__main__':
    palabra: str = "%s "
    lista: list = ["nombre", "apellido_paterno", "nombre_usuario", "edad", "correo_electronico", "contrasennia"]

    print(palabra)
    #palabra = palabra * 5
    print(palabra)

    t=len(lista) #Obtiene el total de elementos de una lista
    print(t)
    palabra=palabra * len(lista)
    print(palabra)

    campos = " & ".join(lista) #"Elefante Perro Gato Leon"
    print(campos)
    palabra= ",".join(palabra)
    print(lista)

    querySQL=f"INSERT INTO tabla ({campos}) VALUES ({palabra})"
    print(querySQL)

