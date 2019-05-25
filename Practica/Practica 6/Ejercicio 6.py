def validacion(n):
    
    while not n - int(n) == 0:
        n = float(input("ERROR!:"))
    
    return int(n)

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
    
    n = float(input())
    n = validacion(n)
    
    while not n == 0:
        
        lista.append(n)
        
        n = float(input())
        n = validacion(n)
    
    
    print("Lista ingresada:")
    print(lista)
    
    print()
    
    print("Lista ordenada:")
    ordenarLst(lista)
    print(lista)
    
    return

main()