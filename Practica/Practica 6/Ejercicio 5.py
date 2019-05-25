import random

def validacion(n):
    
    while not ( n-int(n) == 0 and n>0 ):
        n = float(input(" ERROR! :"))
    
    return int(n)

def cambiarLista(a,b,lst):
    
    if b < a:
        memoria = a
        a = b
        b = memoria

    for i in range(len(lst)):
        
        if not a <= lst[i] <= b:
            lst[i] = random.randrange(a,b+1)
    
    return

def generarLista():
    
    lst=[]
    
    for i in range(5):
        lst.append(random.randrange(35))
    
    return lst




def main():
    
    lista = generarLista()
    print("Lista generada: ")
    print(lista)
    print()
    
    a = float(input("Ingrese limite A del rango: "))
    a = validacion(a)
    b = float(input("Ingrese limite B del rango: "))
    b = validacion(b)
    
    cambiarLista(a,b,lista)
    
    print(lista)
    
    return

main()