if __name__ == '__main__':
    n1=input("Proporciona un nombre: ")
    n2=input("Proporciona otro nombre: ")

    t1=len(n1)
    t2=len(n2)

    if t1 == t2:
        print(F"Los nombres {n1} y {n2} son iguales")
    else:
         if t1>t2:
            print(F"El mayor es {n1}")
         else:
            if t2 > t1:
              print(F"El mayor es {n2}")


