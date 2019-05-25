def validacion(n):
    
    while not ( n%2 == 1 and n >= 5):
        n = int(input("INGRESAR NUMERO IMPAR Y MAYOR O IGUAL A CINCO: "))
    
    return n

def dibujarRombo(diagonal):
    
    for fila in range(diagonal):
        
        for columna in range(diagonal):
            
            if  (columna + fila >= diagonal//2 and columna - fila <= diagonal//2) and ( fila + columna <= (diagonal - 1) + diagonal//2 and fila - columna <= diagonal//2):
                print("*", end = "")
            else:
                print(" ", end = "")
    
        print()

    return


def main():
    
    diagonal = int(input("Ingresar diagonal: "))
    diagonal = validacion(diagonal)
    
    dibujarRombo(diagonal)
    
    return

main()