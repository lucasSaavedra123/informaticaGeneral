def esLetra(l):
    return 'a' <= l <= 'z' or 'A' <= l <='Z' or l in 'ÁÉÍÓÚáéíóú' and not l in '0123456789'

def lMayuscula(t, i):
    
    l = t[i]
    
    if 'a' <= l <= 'z' or l in 'aéíóú':
        l = chr( ord(t[i]) - 32  )
 
    return t[:i] + l + t[i+1:]

def tMayuscula(t):
    
    i = 0
    ancho = len(t)
    
    while i < ancho :
        
        while i < ancho and not esLetra(t[i]):
            i+=1
        
        if i < ancho and esLetra(t[i]):
            t = lMayuscula(t, i)
            
        while i < ancho and esLetra(t[i]):
            i+=1
    
    
    return t


def main():
    
    texto = input("Ingrese un texto: ")
    print("La funcion ha retornado: {}".format(tMayuscula(texto)))
    
    return

main()