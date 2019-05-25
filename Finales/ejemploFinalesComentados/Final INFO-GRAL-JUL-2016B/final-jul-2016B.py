# ACTUALIZADO EL 2017/11/29
# marianotrigila@gmail.com

#Ejercicio 3

# abrir cada archivo y guardar cada uno en un diccionario o en una lista (según conveniencia)
def cargarDicHabitantes():
    archHab = open("habitantes.txt","r")# abrir archivo
    dicHab={}                           # crear dicionario vacia
    for linea in archHab.readlines():   # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")          # de string a lista
        if linea[0]!='':                # condicional para no cargar las lineas que sólo tienen caracteres especiales (ej: \n)
            # convertir a cada elemento de la lista en su tipo de dato original
            # ya que están asignados como string
            linea[0]=int(linea[0])      # conversión a int
            # la posicion [1] queda como string
            linea[2]=int(linea[2])      # conversión a int
            linea[3]=int(linea[3])      # conversión a float
            dicHab[linea[0]]=[linea[1],linea[2] ,linea[3]] # guardar los elementos leidos en un diccionario
    archHab.close()                     # cerrar archivo
    return dicHab                       # retornar la lista con los datos del archivo

def cargarListaHabitantes():
    archHab = open("habitantes.txt","r") # abrir archivo
    listaHab=[]                          # crear lista vacia
    for linea in archHab.readlines():    # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")           # de string a lista
        if linea[0]!='':
            # convertir a cada elemento de la lista en su tipo de dato original
            # ya que están asignados como string
            linea[0]=int(linea[0])       # conversión a int
            # la posicion  [1] queda como string
            linea[2]=int(linea[2])       # conversión a int
            linea[3]=int(linea[3])       # conversión a int
            listaHab.append (linea)      # guardar la lista "linea" en la lista lisHab (lista de lista)
    archHab.close()                      # cerrar archivo
    return listaHab


def cargarDicLocalidades():
    archLoc = open("localidades.txt","r")# abrir archivo
    dicLoc={}                            # crear diccionario vacia
    for linea in archLoc.readlines():    # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                 # eliminar caracter'\n' del final del string de cada linea

        linea=linea.split(",")           # de string a lista
        if linea[0]!='':                 # condicional para no cargar las lineas que sólo tienen caracteres especiales (ej: \n)
            # convertir a cada elemento de la lista en su tipo de dato original
            # dado que están asignados como string
            linea[0]=int(linea[0])       # conversión a int
            # la posicion [1] queda como string
            linea[2]=int(linea[2])       # conversión a int
            dicLoc[linea[0]]=[linea[1],linea[2]] # guardar los elementos leidos en un diccionario
    archLoc.close()                      # cerrar archivo
    return dicLoc                        # retornar la lista con los datos del archivo

def cargarDicHabXLoc():
    archHabXLoc = open("habitantesXlocalidad.txt","r")# abrir archivo
    dicHabXLoc={}                        # crear diccionario vacia
    for linea in archHabXLoc.readlines():# por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")           # de string a lista
        if linea[0]!='':                 # condicional para no cargar las lineas que sólo tienen caracteres especiales (ej: \n)
            # convertir a cada elemento de la lista en su tipo de dato original
            # dado que están asignados como string
            linea[0]=int(linea[0])       # conversión a int
            linea[1]=int(linea[1])       # conversión a int

            dicHabXLoc[linea[1]]=linea[0]# guardar los elementos leidos en un diccionario
    archHabXLoc.close()                  # cerrar archivo
    return dicHabXLoc                    # retornar la lista con los datos del archivo

def imprimirDic(dic):
    for clave in dic:
        print (clave, ":", dic[clave])

def cantHabitantes(loc,hijos):

    dicLoc=cargarDicLocalidades()            # Cargar el archivo "localidades.txt" en un diccionario
    dicHabXLoc=cargarDicHabXLoc()            # Cargar el archivo "habitantesXlocalidad.txt" en un diccionario
    listaHab=cargarListaHabitantes()         # Cargar el archivo "habitantes.txt" en una lista
    idLoc=-1                                 # Inicializo la variable idLoc, para luego detectar si fue asignado

    # Buscar el id de la localidad que pertenece al nombre de localidad pasado por parámetro
    # Hay que iterar porque el diccionario tiene como clave el id y no el nombre
    for clave in dicLoc:                     # iterar el diccionario localidad
        if dicLoc[clave][0]==loc:
            idLoc=clave                      # asignar clave a una variable
            break                            # sale del ciclo

    if(idLoc!=-1):                           # sólo entrar si encontró el idLoc
        contHab=0                            # inicializar el contador de habitantes para la condición
        for hab in listaHab:                 # Iterar la lista de habitantes
            estaEnDic=dicHabXLoc.get(hab[0]) # verifico si la clave está en el diccionario
                                             # (porque sale error de ejecución si se busca una clave que no existe)
            if hab[2]==hijos and estaEnDic and dicHabXLoc[hab[0]]==idLoc:
                contHab=contHab+1            # incrementar contador si cumple condición

    return contHab                           # retornar contador

def edadXLocalidad():
    dicLoc=cargarDicLocalidades()            # Cargar el archivo "localidades.txt" en un diccionario
    dicHab=cargarDicHabitantes()             # Cargar el archivo "habitantes.txt" en un diccionario
    dicHabXLoc=cargarDicHabXLoc()            # Cargar el archivo "habitantesXlocalidad.txt" en un diccionario
    dicEdadXLoc={}                           # crear diccionario vacio
    for claveLoc in dicLoc:                  # por cada clave de localidad del diccionario de localidad
        edad=0                               # inicializar variable donde se sunarán las edades
        cant=0                               # inicializar la variable que se utiliza para contar los habitantes segun condición
        for claveHab in dicHabXLoc:          # por cada clave de habitante del diccionario habitanteXlocalidad
            if dicHabXLoc[claveHab]== claveLoc: # si coincide la localidad
                edad=edad+dicHab[claveHab][2]# acumular la suma de la edad
                cant=cant+1                  # contar
        if cant>0:                           # es para evitar dividir por cero
            dicEdadXLoc[claveLoc]=edad/cant  # guardar el promedio en un diccionario cuya clave es el id de localidad
    imprimirDicOrdenado(dicEdadXLoc)         # imprimir ordenado el diccionario resultante

def imprimirDicOrdenado(dic):
    orden = sorted(dic)                      # obtener una lista de claves (del diccionario dic) ordenada
    print ("{0:15}{1:15}\n".format("Id Localidad","Promedio Edad")) # Imprimir la cabecera de la tabla de salida
    for clave in orden:                      # iterar la lista ordenada de claves del diccionario
        print ("{0:<15}{1:<15}\n".format(clave, dic[clave])) # Imprimir los datos del diccionario


def main():
    #--------- INICIO PROGRAMA PRINCIPAL ----------#

    localidad='Lujan'  # asigno para testear
    hijos=3            # asigno para testear

    cantHabHijos = cantHabitantes(localidad,hijos)   # Obtener la cantidad de habitantes para una localidad y dada una cantidad de hijos
    print ("La cantidad habitantes que tienen {0} hijos en {1} es: {2}\n".format(hijos,localidad,cantHabHijos)) # Imprimir los datos del diccionario

    edadXLocalidad()

    #---------FIN PROGRAMA PRINCIPAL --------------#

main()                                  # llamada a la función principal. Como es lo unico que está
                                        # en el cuerpo del archivo con capacidad de ejecución
                                        # (entonces se ejecuta)