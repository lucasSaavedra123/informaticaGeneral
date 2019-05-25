"""
Los programas por lo general usan archivos para poder guardar informacion
Una manera eficiente de hacer esto es usar base de datos pero es para otra materia

Se puede escribir o leer archivos

Puede ser archivos binarios

Siempre se abre (se trabaja en el) y despues se cierra.
"""

##Si el archivo no existe, se crea.

archivo = open("datos.txt","w")##Nombre del archivo, letra que tiene un significado (leer o escribir)
                               ##w es de escribir (write). Si el programa no esta creado, aca lo crea con ese nombre
                               ##r es de leer (read). Si el programa no esta creado, aca salta error
                               ##Si se quiere leer y escribir 'w+' 'r+' o 'rw' pero no logran lo mismo
                               ##Estos son modos de apertura
                               ##'w' el archivo se borra y si queda lo que escribi
                               ##'a' logra que lo que estaba en el archivo siga estando y lo que escribr queda 'appendeada', agregar.


##Siempre que se modifica el archivo se pone 'nombre del archivo'.accion()

archivo.write("Saracatunga")
archivo.write("Hola")
archivo.write("Hola")
archivo.write("Hola")
archivo.write("Hola")

archivo.write("Hola\n")
archivo.write("Hola\n")
archivo.write("Hola\n")
archivo.write("Hola\n")
archivo.write("Hola\n")

lista = ['so vo', 're loco' , 'crack']

archivo.writelines(lista)

archivo.close()

##Si queres leer

archivo = open("datos.txt", "r")

print(archivo.readline(),end="")##Sin el "" el programa al leer interpreta otra cosa 
print(archivo.readline(),end="")
print(archivo.readline(),end="")
print(archivo.readline(),end="")##Lee linea por linea

print(archivo.readlines())##devuelve lista. Imprime la lisra junto con un \n

##Si queremos sacar el \n de las lineas hacemos slice [:-1] y vamos guardando todo en una nuev alista


archivo.close()##Se cierra el archivo

##Si el archivo esta en otra carpeta se tiene que llevar el nombre del archivo a una ubicacion C:ldfe/jfweofj/eofoe/tecto.txt


##Los archivos .csv separan la informacion en comas

archivo = open("Book1.csv",'r')

"""
for renglon in archivo:
    print(renglon.split(';')) split va cortando a la lista o renglon hasta el simbolo que le damos y saca todo los ; y se queda con esa informacion
"""

for renglon in archivo:
    print(renglon[:-1].split(';'))

##Recordar que si sacamos numeros hay que pasarlos a enteros

##with ... as ... es para ahorrar cerrar un archivo por ejemplo
     ##SIempre va open 
with open("datos.txt") as datos:
    ###PROGRAMA
    ###LO CIERRA Y SE VA
    print("HOla")
   
##open() quiere arbri un archivo con esa intencion y el sistema operativo te da el permiso o no
##Si un archivo es leido a la vez por otros programas no hay problema
##Pero no pueden escribir todos al mismo tiempo
##Empezar a escribir es lento pero escribir no
##El .close() es para decirle al sistema operativo que ya no usas el archivo. Ya trabajaste con el
    
    ##Los archivos binarios no tienen texto y tienen datos expresados en binarios
    ##Python reduce la diferencia entre archivos de texto y binarios.
    ##Otros lenguajes no logran esta diferencia
    ##CUando se escribe en un archivo de texto un numero, le hace la correspondencia
    ## al numero del caracter. Es decir, el numero '458877', cada uno es un texto.
    ##Cada numero es un caracter.
    ##jpg es un archivo binario, por ejemplo.
    ##Las fotos y las imagenes son archivos binarios. Cada pixel ocupa un byte.
    ##QUe es un byte? 8 bits.
    ##
    ##----------------------
    ##| R | V | A  | Alpha | (EJEMPLO, NO ES REAL)
    ##----------------------
    ##
    ##Cada parte es un byte.
    ##R: Rojo
    ##V: Verde
    ##A: Azul
    ##ALpha: Nivel de transparencia.
##Al trabajar con archivos binarios se trabaja asi
    
    """

ar = open('foto.jpg', 'rb')
r = ar.read(1) ##El uno significa que lee cada un byte

while r!='':
    v=ar.read(1)
    a=ar.read(1)
    
    dibujarPixel(r,v,a)
    r=ar.read(1)

"""

##Si queremos escribir
    
"""

ar=open('arch.bin','wb')
listaDeBytes=['\x89','\x122']

for byte in listaDeBytes:
ar.write(byte)

ar.close()

"""