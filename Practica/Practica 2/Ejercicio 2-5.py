import random

def generador(i,s):
    numero = random.randint(i,s)    
    return numero

def main():
    
    indice = 1
    inferior = int(input("Ingrese el limite inferior (numero natural): "))
    superior = int(input("Ingrese el limite superior (numero natural): "))

    numero = generador(inferior, superior)
    print("{0}-Limite inferior {1}, limite superior {2}. Numero generado: {3}".format(indice,inferior,superior,numero))
    indice = indice + 1
    inferior = numero
    
    numero = generador(inferior, superior)
    print("{0}-Limite inferior {1}, limite superior {2}. Numero generado: {3}".format(indice,inferior,superior,numero))
    indice = indice + 1
    superior = numero

    numero = generador(inferior, superior)
    print("{0}-Limite inferior {1}, limite superior {2}. Numero generado: {3}".format(indice,inferior,superior,numero))

    return

main()