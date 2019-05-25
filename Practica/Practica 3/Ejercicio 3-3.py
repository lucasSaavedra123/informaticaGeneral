def tipoDeNumero(n):
    if n/int(n) != 1:
        return "real"
    
    else:
        if n >= 0:
            return "natural"
    
        else:
            return "entero"
        
def signo(n):
    if n < 0:
        return "negativo"
    
    if n > 0:
        return "positivo"
    
    else:
        return "cero"

def main():
    
    numero = float(input("Ingrese un numero: "))
    print("El numero es {} y {}.".format(signo(numero), tipoDeNumero(numero)))
    
    return

main()