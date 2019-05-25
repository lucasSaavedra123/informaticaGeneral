def trabajarPalabra(palabra):
    
    i=0
    palabra2=list(palabra)
    
    while i<len(palabra2):
        
        if 'A'<=palabra[i]<='Z':
            palabra2[i]=chr(ord(palabra2[i])+32)

        i+=1
        
    while ',' in palabra2:
        palabra2.remove(',')
    
    while '-' in palabra2:
        palabra2.remove('-')
    
    while '.' in palabra2:
        palabra2.remove('.')
    
    while '"' in palabra2:
        palabra2.remove('"')
        
    while ';' in palabra2:
        palabra2.remove('"')
        
    palabra = ''
    
    i=0
    
    while i<len(palabra2):
        palabra=palabra+palabra2[i]
        i+=1
    
    
    return palabra


def frecuenciaPalabra(texto,informe):
    
    i=0
    i2=0
    contador = 0
    palabras = []
    textoLineas = texto.readlines()
    
    while i<len(textoLineas):
        
        if textoLineas[i][-1]=='\n':
            textoLineas[i]=textoLineas[i][:-1]
        
        textoLineas[i]=textoLineas[i].split(' ')
        
        i+=1
        
    i=0
    
    ##Sacamos los simbolos de mas y vamos agregando las palabras
    
    while i<len(textoLineas):
        
        while i2<len(textoLineas[i]):
            
            ##Se sacan las comas, comillas, punta y coma, etc.
            textoLineas[i][i2]=trabajarPalabra(textoLineas[i][i2])
            palabras.append(textoLineas[i][i2])
            
            i2+=1
            
        i+=1
        i2=0
    
    i=0
    i2=0
    
    while '' in palabras:
        palabras.remove('')
    
    print('4')
    print(palabras)
    
    ##Se empieza a escribir el texto
    ##Se va palabra por palabra y se las
    ##va borrando de la lista hasta que esa palabra no este mas en la lista
    
    palabrasAux=palabras[:]
    
    for palabra in palabrasAux:
        
        while palabra in palabras:
            contador+=1
            palabras.remove(palabra)
        
        if not contador == 0:
            informe.write('{},{}\n'.format(palabra,contador))
        
        contador = 0

    
    return
    

def main():
    
    texto = open('cuento.txt', 'r')
    contador = open('frecuencias.csv', 'w')
    
    frecuenciaPalabra(texto,contador)
    
    texto.close()
    contador.close()
    
    contador = open('frecuencias.csv', 'r')
    
    print(contador.read())
    
    contador.close()
    
    return

main()