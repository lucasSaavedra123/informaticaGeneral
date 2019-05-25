def validacion(n):
    
    while not (n % 2 != 0 and n >= 5):
        n = int(input("INGRESAR NUMERO IMPAR Y MAYOR O IGUAL A CINCO: "))
    
    return n

def dibujarTriangulo(altura):
    
    print()
    
    for fila in range(altura):
        
        for columna in range(altura):
            
            if fila <= altura - columna - 1 and columna <= fila:
                print("*", end = " ")
            else:
                print(" ", end = " ")

            
        print()
    
        
    return




def main():
    
    altura = int(input("Ingrese altura: "))
    altura = validacion(altura)
    
    dibujarTriangulo(altura)
    
    return

main()