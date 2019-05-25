def verificador (n):
    
    if n % 2 == 0:
        numero_menor= int(input("Ingrese un numero menor que {}: ".format(n)))
        return numero_menor < n ## Devuelve Falso o Verdadero
    else:
        numero_mayor= int(input("Ingrese un numero mayor que {}: ".format(n)))
        return n < numero_mayor

def main():
    
    numero = int(input("Ingrese un numero entero positivo: "))
    
    if verificador(numero):
        print("Correcto!")
    else:
        print("Incorrecto!")
    
    return

main()