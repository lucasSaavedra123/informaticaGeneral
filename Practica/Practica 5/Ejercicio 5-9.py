def esLetra(l):
    return 'a' <= l <='z' or 'A' <= l <= 'Z' or l in 'ÁÉÍÓÚáéíóú'

def darMayor(t):
    
    ancho = len(t)
    i = 0
    pMayor = ''
    
    while i < ancho:
        
        while i < ancho and not esLetra(t[i]):
            i += 1
        
        principio = i
        
        while i < ancho and esLetra(t[i]):
            i += 1
        
        final = i
        
        p = t[principio:final]
        
        if len(pMayor) <= len(p):
            pMayor = p
            
    return pMayor



def darMenor(t):
        
    ancho = len(t)
    i = 0
    pMenor = t
    
    while i < ancho:
        
        while i < ancho and not esLetra(t[i]):
            i += 1
        
        principio = i
        
        while i < ancho and esLetra(t[i]):
            i += 1
        
        final = i - 1
 
        p = t[principio:final+1]
        
        if len(p) <= len(pMenor):
            pMenor = p
            
    return pMenor


def darCantidad(t):
    
    i = 0
    contador = 0
    ancho = len(t)
    
    while i < ancho:
        
        while i < ancho and not esLetra(t[i]):
            i += 1
        
        contador += 1
        
        while i < ancho and esLetra(t[i]):
            i += 1
        
    return contador

def main():
    
    t = input("Ingrese un texto: ")
    print("El texto tiene {} palabras, la de mayor longitud es '{}' y la de menor longitud es '{}'. ".format(darCantidad(t), darMayor(t), darMenor(t)))
    
    return

main()