def operadora (n1,n2,o):
    
    if o == "+":
        resultado = n1+n2
    elif o == "-":
        resultado = n1-n2
    elif o == "*":
        resultado = n1*n2
    elif o == "/":
        resultado = n1/n2
    
    return resultado


def main ():
    numero1= int(input("Ingrese el primer numero: "))
    numero2= int(input("Ingrese el segundo numero: "))
    operacion= input("Ingrese la operacion (+, -, *, /): ")
    
    print("{} {} {} = {:.2f}".format(numero1, operacion, numero2, operadora(numero1, numero2, operacion)))
    
    return

main()