if __name__ == '__main__':
    x=int (input("Ingresa un numero: "))
    y=int (input("Ingresa la potencia: "))

    i:int=1
    poten:int=1

    while i<=y:
        poten=poten*x
        i+=1

    print(F"el resultado de {x}^{y}={poten}")