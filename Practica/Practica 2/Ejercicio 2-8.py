def crearRectangulo(a,h):
    rectangulo = ( crearFila(a) + "\n") * h ## "\n" sirve para indicar el arranque de una nueva linea
    return rectangulo

def crearFila(a):
    linea = "*" * a
    return linea

def main():
    a = 5
    ancho = int(input("Ingrese ancho: "))
    alto = int(input("Ingrese alto: "))
    
    print(crearRectangulo(ancho, alto))
    
    return

main()