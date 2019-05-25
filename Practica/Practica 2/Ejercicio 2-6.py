import random

def booleanGenerator():
    return random.randint(0,1)

def main():

    v=[0,1]
    p=[0,1]
    b=[0,1]

    v[0] = input("Ingrese alternativa 1 para vestimenta: ")
    v[1] = input("Ingrese alternativa 2 para vestimenta: ")
    
    p[0] = input("Ingrese alternativa 1 para plato: ")
    p[1] = input("Ingrese alternativa 2 para plato: ")
    
    b[0] = input("Ingrese alternativa 1 para bebida: ")
    b[1] = input("Ingrese alternativa 2 para bebida: ")

    i = booleanGenerator()
    
    print("Cena al azar: {}, {}, y {}".format(v[i],p[i],b[i]))
    
    return

main()