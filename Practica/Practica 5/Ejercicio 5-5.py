def rotacion(texto):
    return texto[len(texto)//2:len(texto)]+texto[0:len(texto)//2]

def validacion(texto):
    
    while not (len(texto) >= 2 and len(texto) % 2 == 0):
        texto = input("Error. Ingrese un texto: ")
    
    return texto

def main():
    
    texto = input("Ingrese texto: ")
    texto = validacion(texto)
    
    print("La funcion ha retornado: {}".format(rotacion(texto)))
    
    return

main()