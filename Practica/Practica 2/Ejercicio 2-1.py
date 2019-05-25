import math
    
def areaTriangulo(l1,l2,l3):
    area = math.sqrt( math.fsum([l1,l2,l3]) / 2 ) ##fsum logra la suma de los numeros que se le dan y devuelve el resultado
    return area

def main():
    lado1 = int(input("Ingrese el lado 1 (cm): "))
    lado2 = int(input("Ingrese el lado 2 (cm): "))
    lado3 = int(input("Ingrese el lado 3 (cm): "))
    
    print("El area del triangulo es {:.2f}".format(areaTriangulo(lado1,lado2,lado3)))
    return

main()