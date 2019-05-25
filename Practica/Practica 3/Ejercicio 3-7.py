def promedio (n1,n3):
    return (n1+n3) / 2

def verificador(n1,n2,n3):
    
    if n1 > n2:
        num_aux = n1
        n1 = n2
        n2 = num_aux
        
    elif n1 > n3:
        num_aux = n1
        n1 = n3
        n3 = num_aux
    
    if n2 > n3:
        num_aux = n2
        n2 = n3
        n3 = num_aux
    
    if promedio(n1,n3) == n2:
        return True
    else:
        return False

def main():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))
    
    if verificador(numero1, numero2, numero3):
        print("Están igualmente distanciados!")
    else:
        print("NO Están igualmente distanciados!")
    
    return

main()