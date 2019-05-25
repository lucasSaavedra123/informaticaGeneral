import random

def menorMayor(l):
    return [min(l),max(l)]

def minVal(l):
    
    if l == []:
        return -1
    
    mValor = l[0]
    
    for i in l:
        if i < mValor:
            mValor = i
    
    return mValor

def maxVal(l):
    
    if l == []:
        return -1
    
    mValor = 0
    
    for i in l:
        if i > mValor:
            mValor = i
    
    return mValor

def validacion(n):
    
    while not ( n-int(n) == 0 and n>0 ):
        n = float(input(" ERROR! :"))
    
    return int(n)

def cargarListaAleat(a,b,can):
    
    lista = []
    i = 0
    
    if a > b:
        memoria = a
        a = b
        b = memoria

    while i < can:
        lista.append(random.randrange(a,b))
        i +=1
    
    return lista

def main():
    
    lista = []
    
    lista.append(validacion(float(input("Ingrese el 1° extremo del intervalo: "))))
    lista.append(validacion(float(input("Ingrese el 2° extremo del intervalo: "))))
    lista.append(validacion(float(input("Ingrese la cantidad de numeros a guardar: "))))
    
    lista = cargarListaAleat(lista[0],lista[1],lista[2])

    print("Menor numero: {}".format(menorMayor(lista)[0]))
    print("Mayor numero: {}".format(menorMayor(lista)[1]))
    
    print("Menor numero: {}".format(minVal(lista)))
    print("Mayor numero: {}".format(maxVal(lista)))
    
    return

main()