def invertir(n):

    invertido = 0
    
    while n != 0:
        resto = n%10
        n = n*10 + resto
        auxiliar = auxiliar//10

    return invertido

def verificarCapicua (n):

    if invertir(n) == n:
        return True
    else:
        return False

def validacion(n):
    
    while len(n) > 9 or int(n) <= 0:
        n = input("ERROR! Ingrese un numero ENTERO POSITIVO y de hasta NUEVE CIFRAS: ")
        
    return n

def verificarCapicua (n):

    if invertir(n) == int(n):
        return True
    else:
        return False

def main():
    
    numero = input("Ingrese un numero de hasta nueve cifras: ")
    numero = validacion(numero)
    
    if verificarCapicua(int(numero)):
        print("\nEl número es capicua.")
    else:
        print("\nEl número no es capicua.")
    
    return

main()