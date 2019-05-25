def invertir(nStr):

    nStr2 = ""

    for seleccionador in range(len(nStr)-1, -1 , -1):
        nStr2 += nStr[seleccionador]

    return nStr2


def validacion(nStr):
    
    while len(nStr) > 9 or int(nStr) <= 0:
        nStr = input("ERROR! Ingrese un numero ENTERO POSITIVO y de hasta NUEVE CIFRAS: ")
        
    return nStr

def verificarCapicua (nStr):

    if invertir(nStr) == nStr:
        return True
    else:
        return False

def main():
    
    numeroString = input("Ingrese un numero de hasta nueve cifras: ")
    numeroString = validacion(numeroString)
    
    if verificarCapicua(numeroString):
        print("\nEl número es capicua.")
    else:
        print("\nEl número no es capicua.")
    
    return

main()