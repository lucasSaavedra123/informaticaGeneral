def extraerTexto():
    
    archivo = open('info.txt','r')
    cad = archivo.readlines()
    archivo.close()
    cad = cad[0]
    
    if cad[-1] == '\n':
        cad = cad[:-1]
    
    return cad
    

def buscarS(xs,s):
    
    indicePrincipal=0
    indiceFinal=0
    texto = ''
    
    if s not in xs:
        return (-1,-1)
    
    for i in range(len(xs)):
        
        if xs[i] == s[0]:
            
            indicePrincipal = i
            
            for ix in range(i,i+len(s)):
                texto = texto + xs[ix]
                
            indiceFinal = ix
            
            if texto == s:
                return (indicePrincipal,indiceFinal)
            
            texto = ''
    
def transformarPalabra(xs,posicion):
    return xs[:posicion[0]]+' '+xs[posicion[1]+1:]

def indiceLista(s,xs):
    
    lista=[]
    
    while s in xs:
        tupla = buscarS(xs,s)
        lista.append(tupla)
        xs = transformarPalabra(xs,tupla)
    
    return lista

def main():
    s=input('Ingrese string a buscar: ')
    ##print('se encuentra en: {}'.format(buscarS(extraerTexto(),s)))
    print(indiceLista(s,extraerTexto()))
    return

main()
