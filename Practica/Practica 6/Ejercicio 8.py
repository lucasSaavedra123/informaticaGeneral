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



def main():
    
    lista = []
    
    n = float(input("Ingrese los valores a cargar (finalice con '0'):"))
    n = validacion(n)
    
    while not n == 0:
        
        inserOrd(lista,n)##Se van ordenando y se van cargando
        
        n = float(input())
        n = validacion(n)
    
    print()
    print("Lista generada:")
    print(lista)
    
    return

main()
