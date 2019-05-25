def ordenar (n1,n2,n3):
    
    if n1 > n2:
        num_aux = n1
        n1 = n2
        n2 = num_aux
    
    if n1 > n3:
        num_aux = n1
        n1 = n3
        n3 = num_aux
        
    if n2 > n3:
        num_aux = n2
        n2 = n3
        n3 = num_aux
        
    print(n1)
    print(n2)
    print(n3)

    return

def main ():
    
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    numero3 = int(input("Ingrese el tercer numero: "))
    

    print("Los numeros ordenados en forma ascendente son: ")
    ordenar(numero1, numero2, numero3)
    
    return

main()