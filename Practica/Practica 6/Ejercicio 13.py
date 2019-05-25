def agregarDicEle(n,p,dic):
    dic[n] = p 
    return

def imprimirTraduccion(n,dic):
    return print("{} -> {}".format(n,dic[n]))

def main():

    dic = {}

    numero = int(input("Ingrese el numero (termine la carga con un 0): "))
    
    while not numero == 0:

        while numero in dic.keys():
            numero = int(input("ERROR! Ya ha ingresado ese numero. Ingrese el numero (termine la carga con un 0): "))

        palabra = input("Ingrese el numero en palabras: ")
        agregarDicEle(numero,palabra,dic)
        
        numero = int(input("Ingrese el numero (termine la carga con un 0): "))

    print()

    numero = int(input("Ingrese el numero a traducir o cero para salir: "))
    
    while not numero == 0:
        
        while numero not in dic.keys() and not numero == 0:
            numero = int(input("ERROR! Ingrese el numero a traducir o cero para salir: "))

        if numero in dic.keys():
            print()
            imprimirTraduccion(numero,dic)

        if not numero == 0:
            numero = int(input("Ingrese el numero a traducir o cero para salir: "))

    return

main()