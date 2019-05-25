def validacion(n):    
    while not n - int(n) == 0:
        n = float(input("ERROR!:"))
    
    return int(n)


def inserOrd(lst,num):
    i = 0

    while i<len(lst):
        
        if lst[i] > num:
            return lst.insert(i,num)
        
        i+=1
    
    ##Si se llega hasta el final de la lista
    return lst.append(num)


def ordenarLst(lst):
    
    for i in range(len(lst)):
        for ix in range(len(lst)):
            
            if lst[i] < lst[ix]:
                memoria = lst[i]
                lst[i]  = lst[ix]
                lst[ix] = memoria

    return

def main():
    
    lista = []
    
    n = float(input("Ingrese los valores a cargar (finalice con '0'):"))
    n = validacion(n)
    
    while not n == 0:
        
        lista.append(n)
        
        n = float(input())
        n = validacion(n)
    
    print("Lista generada:")
    ordenarLst(lista)
    print(lista)
    
    n = float(input("Ingrese​ ​valor​ ​a​ ​insertar: ​"))
    n = validacion(n)
    
    print("Lista generada:")
    inserOrd(lista,n)
    print(lista)
 
    return

main()