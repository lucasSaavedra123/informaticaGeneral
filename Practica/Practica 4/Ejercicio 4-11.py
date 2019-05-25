def validacion(n):
    
    while n < 2 or n-int(n) != 0:
        n = float(input("ERROR! Ingrese un numero MAYOR O IGUAL a 2: "))
    
    return int(n)

def dibujar(base, altura):
    
    print()

    for fila in range(altura):
        
        for columna in range(base):
        
            if fila == 0 or fila == altura-1 or columna == 0 or columna == base-1:
                print("*", end = "" )
            else:
                print(" ", end = "")
    
        print()
    
    return


def main():

    base = float(input("Ingrese base: "))
    base = validacion(base)
    altura = float(input("Ingrese altura: "))
    altura = validacion(altura)
    
    dibujar(base, altura)
    
    return

main()