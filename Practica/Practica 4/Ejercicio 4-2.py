def validacion (n):

    while n < 0 or n - int(n) != 0:
        n = float(input("ERROR! Ingrese solamente valorees POSITIVOS y ENTEROS: "))
    
    return n

def main ():
    
    numeroMayor = 0
    numeroMenor = 0
    
    numero = float(input("Ingrese numeros enteros positivos (finalice con 0): "))
    numero = validacion(numero)

    numeroMenor = numero ##PARA TOMAR COMO REFERENCIA

    while numero != 0:

        if numero <= numeroMenor:
            numeroMenor = numero
        elif numero > numeroMayor:
            numeroMayor = numero
            
        numero = float(input())
        numero = validacion(numero)
    
    
    if numeroMayor == 0 and numeroMenor == 0 :
        print("No se ha ingresado ningun numero")
    elif numeroMayor == numeroMenor:
        print("Se han ingresado todos los numeros iguales")
    elif numeroMayor == 0 and numeroMenor != 0:
        print("Se ha ingresado un ùnico numero que es {}".format(int(numeroMenor)))
    else:
        print("El mayor es {} y el menor es {}.".format(int(numeroMayor), int(numeroMenor)))
    
    return

main()