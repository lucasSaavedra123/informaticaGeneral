def validacion(n):
    
    while(n > 1000 or n < 0):
        n = int(input("Ingrese un numero MENOR a 1000 y POSITIVO: "))
    
    return n

def aBinario (n):
    
    suma = 0
    contador = 0
    
    while not (n//2 == 0 and n != 1): ##Se pone distinto a uno para que aun siga considerando la divison de 1 con dos pq sino el while para hasta que de 1 y no tiene que ser asi
        
        suma = ( n % 2 ) * (10**contador) + suma
        n = n // 2
        contador = contador + 1    
        
    return suma

def main():
    
    numero = int(input("Ingrese un numero decimal: "))
    numero = validacion(numero)
    
    print("Numero en binario: {} ".format(aBinario(numero)))
    
    return

main()