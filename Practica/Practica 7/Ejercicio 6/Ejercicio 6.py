import random


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
        palabra2.remove(';')
        
    while '(' in palabra2:
        palabra2.remove('(')

    while ')' in palabra2:
        palabra2.remove(')')
    
    while ':' in palabra2:
        palabra2.remove(':')   
        
        
    palabra = ''
    
    i=0
    
    while i<len(palabra2):
        palabra=palabra+palabra2[i]
        i+=1
    
    return palabra

def generadora(ori,dest,cant):
    
    origen = open(ori,'r')
    destino = open(dest,'w')
    
    i=0
    contador = 0
    palabras = []
    palabrasUsadas = []
    lineas = origen.readlines()
    
    for i in range(len(lineas)):
        if lineas[i][-1]=='\n':
            lineas[i]=lineas[i][:-1]
    
    for i in range(len(lineas)):
        lineas[i]=lineas[i].split(' ')
    
    for i in range(len(lineas)):
        for ix in range(len(lineas[i])):
            if not lineas[i][ix] in palabras:
                palabra=trabajarPalabra(lineas[i][ix])
                palabras.append(palabra)
    
    while '' in palabras:
        palabras.remove('')
    
    
    while contador < cant:
        
        iAleat = random.randrange(len(palabras))
        
        if not palabras[iAleat] in palabrasUsadas:
            destino.write("{}\n".format(palabras[iAleat]))
            
            palabrasUsadas.append(palabras[iAleat])
            contador +=1
            
    
    origen.close()
    destino.close()
    
    return

def main():
    generadora('origen.txt','destino.txt',10)
    return

main()