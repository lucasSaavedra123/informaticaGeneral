def esLetra(l):
    return 'a' <= l <= 'z'

def procesar(t,p):
    
    i = 0
    
    while i < len(t):
        
        contador = 0
        
        while i < len(t) and not esLetra(t[i]):
            i += 1
            
        principio = i
        
        while i < len(t) and esLetra(t[i]):
            i += 1
    
        final = i
        
        px = t[principio:final]
        
        
        if len(px) == len(p):
            
            for ix in range(len(px)):
                if px[ix] in p:
                    contador += 1 
        
            if contador == len(p):
                return True
    
    return False

def main():
    
    t = input("Ingresar el texto: ")
    p = input("Ingresar la palabra: ")
    
    if procesar(t,p):
        print("Se cumple la condicion.")
    else:
        print("No se cumple la condicion.")
    
    return

main()