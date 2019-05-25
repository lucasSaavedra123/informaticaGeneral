def agregarMedia(archivo):

    i = 0
    i2 = 0
    suma = 0
    lineas = archivo.readlines()
    lineasL = lineas[:len(lineas)]
    ##Se imprimen los datos
    print(lineasL)    
    print(lineas)
    ##Se saca \n
    while i < len(lineas):
        lineas[i]=lineas[i][:-1].split(';')
        i+=1
        
    i = 0
    
    print(lineas)
    print(lineasL)
    ##Se convierte los numeros en enteros
    while i < len(lineas):
        while i2 < len(lineas[i]):
            ##Se pregunta antes si hay una cadena vacia por las dudas. Pasa a ser 0 este espacio
            if not lineas[i][i2]=='':
                lineas[i][i2]=int(lineas[i][i2])
                i2+=1
            else:
                del lineas[i][i2]
            
        i2=0
        i+=1
    
    print(lineas)
    
    archivo.close()
##SE IMPRIME EN EL ARCHIVO TODO

    archivo = open('numeros8.csv', 'w')

    i=0
    i2=0
        
    while i < len(lineas):
          
        while i2<len(lineas[i]):
          suma = suma + lineas[i][i2]
          i2+=1
            
        archivo.write(lineasL[i])
        archivo.write('{}\n'.format(str(suma//len(lineas[i]))))
        
        i2=0
        i+=1
        suma=0
    
    
    
    return    


def main():

    archivo = open('numeros8.csv', 'r+')
    agregarMedia(archivo)
    archivo.close()

    return

main()