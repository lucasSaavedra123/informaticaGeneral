def esLetra(l):
    return 'a' <= l <= 'z' or 'A' <= l <= 'Z' or l in 'áéíóúÁÉÍÓÚ'

def contador(tLargo, tCorto):
    
    i = 0
    contador = 0
    
    while i < len(tLargo):
        
        while i < len(tLargo) and not esLetra(tLargo[i]):
            i += 1
            
        principio = i
        
        while i < len(tLargo) and esLetra(tLargo[i]):
            i += 1
            
        final = i
        
        if tCorto == tLargo[principio:final]:
            contador += 1
    
    return contador

def main():
    
    texto1 = input("Ingrese el texto largo:")
    texto2 = input("Ingrese el texto corto:")
    
    print("El texto corto se encontró {} veces en el texto largo.".format(contador(texto1,texto2)))
    
    return

main()