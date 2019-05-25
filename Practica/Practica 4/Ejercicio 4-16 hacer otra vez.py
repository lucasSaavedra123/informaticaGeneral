def validacion(n):
    
    while not ( n%2 == 1 and n >= 7):
        n = int(input("INGRESAR NUMERO IMPAR Y MAYOR O IGUAL A SIETE: "))
    
    return n

def dibujarFigura(a):

    for posicionVertical in range(a-2,0,-2):

        print("*", end = "")
        
        for posicionHorizontalEspacio in range( (a - posicionVertical) // 2 - 1 ):
            print(" ", end = "")
        
        for posicionHorizontalAsterico in range(posicionVertical):
            print("*", end = "")
            
        for posicionHorizontalEspacio in range( (a - posicionVertical) // 2 - 1 ):
            print(" ", end = "")
            
        print("*", end = "")
        print()

    for posicionHorizontal in range(a):  
            print("*", end = "")
    
    return


def main():
    
    ancho = int(input("Ingresar ancho: "))
    ancho = validacion(ancho)
    
    dibujarFigura(ancho)
    
    return

main()