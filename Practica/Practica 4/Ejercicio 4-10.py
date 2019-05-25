def validacion(n):
    
    while n < 2 or n-int(n) != 0:
        n = float(input("ERROR! Ingrese un numero MAYOR O IGUAL a 2: "))
    
    return int(n)

def dibujar(b, a):
    
    for posicionVertical in range(a):
        
        print()
        
        for posicionHorizontal in range(b):
            print("*", end = " ")
        
    return



def main():
    
    base = float(input("Ingrese base: "))
    base = validacion(base)
    altura = float(input("Ingrese altura: "))
    altura = validacion(altura)
    
    dibujar(base, altura)
    
    return

main()