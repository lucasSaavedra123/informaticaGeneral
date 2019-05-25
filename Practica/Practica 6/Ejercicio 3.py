def estaEnLista(l,n):
    return n in l

def validacion(l,n):
    while estaEnLista(l,n):
        n = input("ERROR. Ingresar valores enteros positivos y no lo repita: ")
    
    return n

def cargarLista(l,n):
    return l.append(n)

def cargarConjuntos(l1,l2):
    
    n = input("Ingrese valores para la lista 1 (para terminar escriba '0'): ")
    n = validacion(l1,n)
    
    while not n == '0':
        cargarLista(l1,n)
        n = validacion(l1,input())
    
    n = input("Ingrese valores para la lista 2 (para terminar escriba '0'): ")
    n = validacion(l2,n)
    
    while not n =='0':
        cargarLista(l2,n)
        n = validacion(l2,input())
    
    return

def lstUnion(l1,l2):
    
    lista = []
    
    for i in l1:
        if not i in lista:
            lista.append(i)

    for i in l2:
        if not i in lista:
            lista.append(i)
    
    return lista
    
def lstInterseccion(l1,l2):
    
    lista = []
    
    for i in l1:
        if i in l2:
            lista.append(i)
    
    return lista

def lstDif(l1,l2):
    
    lista =[]
    
    for i in l1:
        if not i in l2:
            lista.append(i)
    
    return lista

def lstDifSimetrica(l1,l2):
    
    lista = [] 

    for i in l1:
        if not(i in l2 or i in lista ):
            lista.append(i)

    for i in l2:
        if not(i in l1 or i in lista ):
            lista.append(i)

    return lista


def mostrarMenu():
    
    n = '0'

    while not ('1' <= n <= '6'):
    
        print("1. CARGAR CONJUNTOS")
        print("2. UNION")
        print("3. INTERSECCION")
        print("4. DIFERENCIA (A-B)")
        print("5. DIFERENCIA SIMÉTRICA")
        print("6. SALIR")
        
        print()
        n = input("Ingrese el valor de la opcion: ")
        print()
        
    return n

def mostrarLista(l1,l2):
    print("Lista 1: {}".format(l1))
    print("Lista 2: {}".format(l2))

def main():
    
    lista1 = []
    lista2 = []
    
    n = mostrarMenu()
    
    while not n == 6:
        
        print()
        
        if n=='1':
            cargarConjuntos(lista1,lista2)
            mostrarLista(lista1,lista2)
        elif n=='2':
            print("UNION: {}".format(lstUnion(lista1,lista2)))
        elif n=='3':
            print("INTERSECCION: {}".format(lstInterseccion(lista1,lista2)))
        elif n=='4':
            print("DIFERENCIA: {}".format(lstDif(lista1,lista2)))
        elif n=='5':
            print("DIFERENCIA SIMETRICA: {}".format(lstDifSimetrica(lista1,lista2)))
            
        print()
        n = mostrarMenu()

    print("Gracias por usar el programa!")
    return

main()