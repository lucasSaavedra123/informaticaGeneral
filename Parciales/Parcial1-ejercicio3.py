def main():
    
    esAscendente = False
    esDescendente = False
    sonIguales = False
    seRompioOrden = False
    
    numeroIngresado1 = int(input())
    numeroIngresado2 = int(input())
    
    if(numeroIngresado2 > numeroIngresado1):
        esAscendente = True
    elif(numeroIngresado2 < numeroIngresado1):
        esDescendente = True
    else:
        sonIguales = True
        
    numeroIngresado1 = numeroIngresado2
    numeroIngresado2 = int(input())
    
    while(numeroIngresado2 != 0):
        if(seRompioOrden == False):        
            if(numeroIngresado1 > numeroIngresado2 and (esAscendente or sonIguales)):
                seRompioOrden = True;
            elif(numeroIngresado1 < numeroIngresado2 and (esDescendente or sonIguales)):
                seRompioOrden = True;
            
        
        numeroIngresado1 = numeroIngresado2
        numeroIngresado2 = int(input())
        
    if(seRompioOrden):
        print("No hay datos")
    elif(esDescendente):
        print("Es Descendente")
    elif(esAscendente):
        print("Es Ascendente")
    elif(sonIguales):
        print("Son iguales")


    return


main()