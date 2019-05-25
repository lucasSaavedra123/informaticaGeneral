def factorizar(n):
    
    if n == 0:
        print("El factorial de {} es: 1".format(n))
    elif n < 0:
        print("No se puede calcular el factorial de un número negativo.")
    else:
        factorial = n
        contador = n
        
        while not contador == 1:
            contador -= 1
            factorial = factorial * contador
        
        print("El factorial de {} es: {}".format(n, factorial))
    
    
    return

def main():
    
    numeroEntero = int(input("Ingrese un número entero: "))
    factorizar(numeroEntero)
    
    return

main()