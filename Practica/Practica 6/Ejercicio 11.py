import random

def validacion(n):
    
    while not (n - int(n) == 0 and n > 0):
        n = float(input("ERROR!:"))
    
    return int(n)

def cargarListaAleat(a,b,can):
    
    lst = []
    i = 0
    
    if a > b:
        memoria = a
        a = b
        b = memoria

    while i < can:
        lst.append(random.randrange(a,b))
        i +=1
    
    return lst

def porcentual(lst):

    numeros = []
    veces = 0
    total =  len(lst)
    
    for i in lst:
        if not i in numeros:
            numeros.append(i)
            
            for ix in lst:
                if i == ix:
                    veces+=1
            
            if veces == 1:
                print("El numero {} salió {} vez ({}%)".format(i,veces,int((veces/total)*100)))
            elif veces > 1:
                print("El numero {} salio {} veces ({}%)".format(i,veces,int((veces/total)*100)))
        
            veces = 0
            
    
    return


def ruleta():
    
    n = float(input("Ingrese el numero: "))
    n = validacion(n)
    
    lst = cargarListaAleat(0,36,n)

    return lst


def main():
    
    lista = ruleta()
    print(lista)
    print()
    
    porcentual(lista)
    
    return

main()