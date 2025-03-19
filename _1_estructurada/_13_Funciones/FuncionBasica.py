def suma(a:int,b:int)->int:
    return a+b

def sumaArreglo(lista:list)->int:
    return sum(lista)

if __name__ == '__main__':

    print(f"La suma es {suma(15, 2)}")
    print(f"la suma l arreglo {sumaArreglo([7,8])}")

