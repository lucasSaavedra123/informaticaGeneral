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
    palabra = ''
    
    i=0
    
    while i<len(palabra2):
        palabra=palabra+palabra2[i]
        i+=1
    
    return palabra

def cabecera2(arch,cant,pmin,pmax):
    
    i=0
    contador = 0
    palabras = []
    contPalabras = []
    lista = arch.readlines()
    
    ##Se sacan las '\n'
    for i in range(len(lista)):
        if '\n' in lista[i]:
            lista[i]=lista[i][:-1]
    
    ##Se separa todo por palabras
    for i in range(len(lista)):
       lista[i]=lista[i].split(' ')
       
       
    ##Se extraen las palabras y se las ordena de una mejor manera
    for i in range(len(lista)):
       
       for ix in range(len(lista[i])):
            palabra = trabajarPalabra(lista[i][ix])
            palabras.append(palabra)
       
    ##Se extraen los caracteres vacios
    while '' in palabras:
        palabras.remove('')
    
    ##Se trabajan con las palabras y se va desarrolando el archivo resultados.csv
    
    informe = open('resultados.csv', 'w')
    
    for palabra in palabras:
        
        if contador < cant:
            if pmin <= len(palabra) <= pmax:
                if not palabra in contPalabras:
                    informe.write("{}\n".format(palabra))
                    contador +=1
                    contPalabras.append(palabra)
        
    informe.close()
    
    return

def main():
    
    archivo = open('texto.txt','r')
    cabecera2(archivo,5,1,20)
    archivo.close()
    
    informe = open('resultados.csv', 'r')
    print(informe.read())
    informe.close()
    
    return

main()