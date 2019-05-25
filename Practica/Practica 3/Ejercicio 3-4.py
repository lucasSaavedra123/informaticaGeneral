def verificador(n1,n2):
    
    if n1 < n2:
        num_aux = n1
        n1 = n2
        n2 = num_aux
        
    resultado = n1 - n2
    
    if n2 <= resultado <= n1:
        return True
    else:
        return False

def main():
    
    numero1 = int(input("Ingrese un numero A: "))
    numero2 = int(input("Ingrese un numero B: "))
    
    if verificador(numero1,numero2):
        print("SI cumple condicion")
    else:
        print("NO cumple condicion")    
        
    
    return

main()