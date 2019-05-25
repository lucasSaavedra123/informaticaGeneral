import math

#Calculo el area del circulo
def areaCirculo(d):

    radio = d/2 
    aCirculoMax = math.pow(radio,2) * math.pi
    
    radio = radio/2
    aCirculoMin = math.pow(radio,2) * math.pi
    
    aCirculo = aCirculoMax + aCirculoMin * 2
    math.sqrt(3)
    return aCirculo

#Calculo el area del cuadrado
def areaCuadrado(lCuadrado):
    aCuadrado = math.pow(lCuadrado,2) 
    return aCuadrado

#Calculo el area de la zona negra
def areaNegra(lCuadrado):
    aNegra = areaCuadrado(lCuadrado)-areaCirculo((lCuadrado*8)/12)
    return aNegra

#Programa principal
def main():
    
    lado = int(input("Ingrese el lado del cuadrado: "))
    porcentaje = (areaNegra(lado)/areaCuadrado(lado)) * 100
    
    print("El area negra es {0:.2f} y es un {1:.2f}% del area total del cuadrado.".format(areaNegra(lado), porcentaje))
    
    return

main()