def estaEnLista(l,n):
    return n in l

def cargarLista(l,n):
    return l.append(n)

def validacion(l,n):
    
    while not (n>=0 and n-int(n)==0 and not estaEnLista(l,n)):
        n = float(input("ERROR. Ingresar valores enteros positivos y no lo repita: "))
    
    return int(n)

def main():
    
    lista=[]
    
    n = float(input("Ingrese un valor"))
    n = validacion(lista,n)
        
    while not n == 0:
        
        cargarLista(lista,n)
        
        n = float(input("Ingrese un valor"))
        n = validacion(lista,n)
    
    print("La lista contiene: ")
    print(lista)
    
    return

main()