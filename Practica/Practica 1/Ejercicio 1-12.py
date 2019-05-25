def main():
    
    numero1 = int(input("Ingresar el primer numero: "))
    numero2 = int(input("Ingresar el segundo numero: "))
    numero3 = int(input("Ingresar el tercer numero: "))

    numero = int(numero1) + int(numero2) + int(numero3)

    print("{:=10d}".format(numero1) ) ##:= d hace que ponga el signo a la izquierda de todo (en el caso de ser negativo). si es positivo se pone :=+ d
    print("{:=10d}".format(numero2) )
    print("{:=10d}".format(numero3) )

    print("-" * 10)

    print("{:>10}".format(numero) )

main()