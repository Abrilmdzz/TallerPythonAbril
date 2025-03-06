if __name__ == '__main__':
    x=int (input("Ingresa un numero: "))
    y=int (input("Ingresa el siguiente numero: "))

    r=0
    i=0

    while i<y:
        r+=x
        i+=1
    print(F"el resultado de {x}*{y} es igual a {r}")
