from setuptools.command.egg_info import manifest_maker

if __name__ == '__main__':
    #Funcion que recibe una tupla y la desempaqueta

    def calcular_area(rectangulo: tuple[int, int]) ->int:
        largo, ancho = rectangulo
        return largo * ancho

    def cuadrado(rectangulo: tuple[int, int]) -> tuple [int, int]:
        largo, ancho = rectangulo
        largo = largo * largo
        ancho = ancho * ancho
        return (largo, ancho)

if __name__ == '__main__':
    #Crear la tupla
    dimenciones =(10, 5)
    #Llamar ala funcion con la tupla
    area = calcular_area(dimenciones)
    print(f"El area del rectangulo es: {area} mts. cuadrados")

    largo, ancho = cuadrado((5, 3))
    print(f"Su lago es de: {largo} y su ancho de: {ancho}")