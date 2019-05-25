def validacion(n):
    
    while n < 3 or n-int(n) != 0:
        n = float(input("ERROR! Ingrese un numero MAYOR O IGUAL a 2: "))
    
    return int(n)

def dibujar(base):
    
    for fila in range(base):
        for columna in range(base):
            
            if columna <= fila:
                print("*", end = " ")
            else:
                print(" ", end = " ")
            
        print()
    
    
    return


def main():
    
    base = float(input("Ingrese base: "))
    base = validacion(base)
    
    dibujar(base)
    
    return

main()