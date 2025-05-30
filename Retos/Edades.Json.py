import json
import sys


def Mi_iterador():
    with open("Edades.Json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)


    for persona in datos["Usuarios"]:
        yield (persona["Id"], persona["Nombre"], persona["Edad"], persona["RFC"])


if __name__ == '__main__':

    # Definición de códigos ANSI
    RESET = "\033[0m"  # Restablece el color a su valor por defecto
    # Colores de texto
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    # Colores de fondo
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    i=3
    for id, nombre, edad, RFC in Mi_iterador():

        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(BLUE)
            case 4:
                sys.stdout.write(MAGENTA)
            case 5:
                sys.stdout.write(YELLOW)
            case _:
                sys.stdout.write(RESET)


        print("Usuario:")
        print("Id: ", id)
        print("Nombre: ", nombre)
        print("Edad: ", edad)
        print("RFC: ", RFC)

        if edad >= 18:
            print(f"El usuario {id} es mayor de edad")
        else:
            print(f"El usuario {id} es menor de edad")

        print("-----------------------------")
        i=3

