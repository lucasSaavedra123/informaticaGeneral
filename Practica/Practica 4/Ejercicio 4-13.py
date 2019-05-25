def validacion(n):

    while n < 3 or n % 2 == 0 or n-int(n) != 0:
        n = float(input("Numero no vàlido. Ingrese base: "))
    
    return int(n)

def dibujar(base):
    
    for fila in range(base//2+1):
        
        for columna in range(base):
            
            if  base//2 - fila <= columna <= base//2 + fila :
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