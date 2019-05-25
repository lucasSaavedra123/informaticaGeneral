import math

def raiz(x,n):
    resultado = math.pow(x,1/n) ##math.pow(base,exponente)
    return resultado

def main():
    radicando = int(input("Ingrese el radicando (numero real): "))
    indice = int(input("Ingrese el indice (numero natural):"))

    print("La raiz {0} de {1} es = {2:.7f}".format(radicando, indice, raiz(radicando, indice)))
    
    return

main()