def validacion(n):
    
    while( not len(n) == 4 or int(n) <= 0 or not int(n) - int(n) == 0 ):
        n = input("ERROR! Ingrese solamente un NUMERO de 4 CIFRAS y POSITIVO: ")
        
    return int(n)


def verificador(n):
    
    u  = n % 10
    d  = ( n // 10 ) % 10
    c  = ( n // 100 ) % 10
    um = ( n // 1000 ) % 10
    
    if (u + c == d + um):
        return True
    else:
        return False
    
    
def main():

    numero = input("Ingrese un numero de 4 cifras y positivo:" )
    numero = validacion(numero)
    
    if verificador(numero):
        print("La condición se cumple.")
    else:
        print("La condición no se cumple")
    

    return

main()