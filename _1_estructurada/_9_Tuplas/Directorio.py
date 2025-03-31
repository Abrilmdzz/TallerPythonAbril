if __name__ == '__main__':
    agenda={}

    agenda["GOAT800717"]=("Tomas Gonzales", "csctomasgonzalez@gmail.com", "2224004953")
    agenda["GOAT800719"]=("Luis Gonzales", "Luis85@gmail.com", "2285564596")
    agenda["GOAT800718"]=("Fabiola Gonzales", "fabis25@gmail.com", "22245600496")
    agenda["GOAT800710"]=("Fernando Gonzales", "fergon56@gmail.com", "22240054497")

    nombre, correo, numero = agenda["GOAT800718"]

    print(f"Datos de la persona: {nombre}, {correo} y {numero}")
