def verificar(n):
    
    suma = 0
    contador = 0

    print("\n")
    
    for i in range(1, n):
        
        if n % i == 0:

            if contador < 4:
                contador += 1
                print("{}º Numero Divisible: {}".format(contador, i))
            
            suma = suma + i
    
    
    if suma == n:
        return True
    else:
        return False
    

def validacion(n):

    while n <= 0 or n - int(n) != 0:
        n = float(input("ERROR! Ingrese solamente numeros ENTEROS y POSITIVOS: "))
    
    return n

def main():
    numero = int(input("Ingrese un numero: "))
    numero = validacion(numero)
    
    if verificar(numero):
        print("\nEl numero es perfecto")
    else:
        print("\nEl numero no es perfecto")
    
    return

main()