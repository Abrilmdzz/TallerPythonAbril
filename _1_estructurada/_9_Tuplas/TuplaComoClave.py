if __name__ == '__main__':
    #Usar una tupla como claveen un diccionario
    diccionario = {
        ("Id, int"): '2',
        'nombre': 'Juan',
        'apellido': 'Gutierrez'}

    diccionario={}
    #Agregar tupla como clave
    diccionario[("Ana", 25)] = "Estudiante"
    diccionario[("Luis", 30)] = "Ingeniero"
    diccionario[("Carlos", 40)] = "Abogado"

    #Acceder a los valores del diccionario usando la tupla
    ocupacion_ana = diccionario[("Ana", 25)]
    ocupacion_luis = diccionario[("Luis", 30)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_luis}")
