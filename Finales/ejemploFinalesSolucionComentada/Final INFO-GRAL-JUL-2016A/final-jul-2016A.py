# ACTUALIZADO EL 2018/07/12
# marianotrigila@gmail.com

#Se asume en este ejercicio que los archivos se encuentra "bien formado", es decir cumple con:
# - Todas las lineas tienen datos separados por comas y están completas.
# - Al final de cada linea (todas) hay un '\n'


# Ejercicio 3


# abrir cada archivo y guardar cada uno en una lista
def cargarListavendedores():
    archVen = open("vendedores.txt","r")# abrir archivo
    lisVen=[]                           # crear lista vacia
    for linea in archVen.readlines():   # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")          # de string a lista
        
        # convertir a cada elemento de la lista en su tipo de dato original
        # ya que están asignados como string
        linea[0]=int(linea[0])          # conversión a int
        # la posicion [1] queda como string
        linea[2]=int(linea[2])          # conversión a int
        linea[3]=float(linea[3])        # conversión a float
    
        lisVen.append(linea)            # guardar la lista "linea" en la lista lisVen(lista de lista)
    
    archVen.close()                     # cerrar archivo
    return lisVen                       # retornar la lista con los datos del archivo

def cargarListaVentasTarjetas():
    archVenTar = open("ventasTarjetas.txt","r")# abrir archivo
    lisVenTar=[]                        # crear lista vacia
    for linea in archVenTar.readlines():# por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")          # de string a lista

        # convertir a cada elemento de la lista en su tipo de dato original
        # ya que están asignados como string
        linea[0]=int(linea[0])          # conversión a int
        # la posicion  [1] queda como string
        linea[2]=int(linea[2])          # conversión a int

        lisVenTar.append (linea)        # guardar la lista "linea" en la lista lisVenTar (lista de lista)

    archVenTar.close()                  # cerrar archivo
    return lisVenTar                    # retornar la lista con los datos del archivo

def cargarListaComisiones():
    archComi = open("liquidacionComisiones.txt","r")#abrir archivo
    lisComi=[]                          # crear lista vacia
    for linea in archComi.readlines():  # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")          # de string a lista
        
        # convertir a cada elemento de la lista en su tipo de dato original
        # ya que están asignados como string
        linea[0]=int(linea[0])          # conversión a int
        linea[1]=float(linea[1])        # conversión a float
        
        lisComi.append (linea)          # guardar la lista "linea" en la lista lisComi (lista de lista)

    archComi.close()                    # cerrar archivo
    return lisComi                      # retornar la lista con los datos del archivo

def imprimirLista(lista):
    for linea in lista:
        print(linea)

def comision(cantar,objtar,sueldo):
    # calcular comisión para una cantidad de tarjetas
    # comparando la cantidad de tarjetas "cantar" contra el objetivo de tarjeta "objtar"
    # El valor de la comisión en un porcentaje del sueldo
    porObjMin   = 0.8                   # Porcentaje del objetivo 80 %
    porEsc10    = 0.1                   # Porcentaje 10 %
    porEsc3     = 0.03                  # Porcentaje 3 %
    comisionMin = 0                     # si no cumple con la comisión

    if(cantar<objtar*porObjMin):
        valorComision = comisionMin     # no cumple con la comisión
    elif (objtar*porObjMin<=cantar<objtar):
        valorComision = sueldo*porEsc3  # cumple con la escala 3 de comisión
    else:
        valorComision = sueldo*porEsc10  # cumple con la escala 1 de comisión
    return valorComision

def liquidar():
    # calcula la comisión por cada vendedor y escribe en el archivo liquidacionComisiones.txt
    # el id del vendedor y su correspondiente comisión
    lisVen = cargarListavendedores()       # Cargar el archivo "vendedores.txt" en una lista lisVen
    lisVenTar = cargarListaVentasTarjetas()# Cargar el archivo "ventasTarjetas.txt" en una lista lisVenTar

    archLiqComi = open("liquidacionComisiones.txt","w")  # abrir archivo
    tamVen=len(lisVen)                     # Cantidad de elementos de la lista de vendedores
    tamVenTar=len(lisVenTar)               # Cantidad de elementos de la lista de VentasTarjetas
    for ven in lisVen:                     # iterar la lista de vendedores y guardar cada registro de vendedor en la variable ven
        totTar=0                           # inicializar el total por tarjeta
        for venTar in lisVenTar:           # iterar la lista de VentasTarjetas y guardar cada registro de venta por tarjeta en la variable venTar
            if (ven[0]==venTar[0]):        # comparar si son los mismos codigos de vendedores
                totTar=totTar+venTar[2]    # acumular los totales de tarjetas
        com=comision(totTar,ven[2],ven[3]) # calcular la comisión
        com=round(com, 2)                  # redondeo a dos decimales para no escribir "muchos" decimales en el archivo
        archLiqComi.write(str(ven[0])+","+str(com)+"\n") # escribir en el archivo "liquidacionComisiones.txt" el código del vendedor y el valor de la comisión

def topcinco():
    # obtiene los cinco vendedores que tengan la mayor comision
    # Para ello se ordena la lista y se imprimen los cinco primeros
    lisVen = cargarListavendedores() # Cargar el archivo "vendedores.txt" en una lista lisVen
    lisComi= cargarListaComisiones() # Cargar el archivo "liquidacionComisiones.txt" en una lista lisComi
    cantidad=5                       # cantidad de registros que se necesitan leer e imprimir "de la lista ordenada"

    lisComi=ordenarLista(lisComi,1)  # ordenar la lista lsiComi por el campo 1

    print ("{0:10}{1:10}\n".format("codVen","Comision"))               # Imprimir la cabecera de la tabla de salida
    for i in range(0,cantidad):
        print ("{0:<10}{1:<10}\n".format(lisComi[i][0],lisComi[i][1])) # Imprimir los daots de la lista

def ordenarLista(lista, c):
    # lista: es la lista que se va a ordenar
    # c: es el número de "campo" por el cual se va a ordenar
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j][c] > lista[i][c]: # >: ordena descendente  , <: ordena ascendente
                lista[i] , lista[j] = lista[j] , lista[i]
    return lista

def main():
    #--------- INICIO PROGRAMA PRINCIPAL ----------#

    liquidar()     # Se crea el archivo "liquidacionComisiones.txt" con las comisiones por codigo de vendedor

    topcinco()     # Imprime los primero cinco (codVen y comisión) cuya comisiones sean las mayores

    #---------FIN PROGRAMA PRINCIPAL --------------#


main()                      # llamada a la función principal main(). Como es la unica
                            # llamada a función que está en el cuerpo del archivo 
                            # => es la que se ejecuta
