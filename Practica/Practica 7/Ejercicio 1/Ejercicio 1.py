def valorPromedio(nList):

    if len(nList)==0:
        return 0

    suma = 0

    for n in nList:
        suma = n + suma 
    
    return suma // len(nList)


def cantLineas(nList):
    return len(nList)

def informe(a):

    numeros = a.readlines()
    print(numeros)

    for i in range(len(numeros)):

        if numeros[i][-1] == '\n':
            numeros[i]=int(numeros[i][:-1])
        else:
            numeros[i] = int(numeros[i])

    print(numeros)

    return  [min(numeros),max(numeros),valorPromedio(numeros),cantLineas(numeros)]



def main():

    archivo = open('informe.txt', 'r')
    datos = informe(archivo)

    print("Valor Minimo: {}".format(datos[0]))
    print("Valor Maximo: {}".format(datos[1]))
    print("Valor promedio: {}".format(datos[2]))
    print("Cantidad de lineas: {}".format(datos[3]))
    
    archivo.close()
    
    return

main()