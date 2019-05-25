import random

def validacion(n):
    
    while not n - int(n) == 0:
        n = float(input("ERROR!:"))
    
    return int(n)

def atributoTriple(lst):
    
    contador = 0
    contadorTriples = 0
    i = 1
    
    while i < len(lst):
        
        if lst[i]==lst[i-1]:
            contador +=1
        else:
            if contador == 2:
                contadorTriples+=1
            
            contador = 0
        
        i+=1
        
    if contador == 2:
            contadorTriples+=1
    
    if contadorTriples == 0:
        return "NADA"
    elif contadorTriples == 2:
        return "Dos Triple"
    elif contadorTriples == 1:
        return "Un Triple"
    elif contadorTriples >= 3:
        return "+ Triple"

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




def main():
    
    a = float(input("Ingresar extremo: "))
    a=validacion(a)
    
    b = float(input("Ingresar el otro extremo: "))
    b=validacion(b)
    
    can = float(input("Ingresar la cantidad de numeros: "))
    can=validacion(can)
    
    lista = cargarListaAleat(a,b,can)
    print(lista)

    print(atributoTriple(lista))
    
    return

main()