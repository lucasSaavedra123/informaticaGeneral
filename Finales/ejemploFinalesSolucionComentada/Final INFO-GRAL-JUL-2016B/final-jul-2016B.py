# ACTUALIZADO EL 2018/07/15
# marianotrigila@gmail.com

#Se asume en este ejercicio los archivos se encuentra "bien formado", es decir cumple con:
# - Todas las lineas tienen datos separados por comas y están completas.
# - Al final de cada linea (todas) hay un '\n'

#Ejercicio 3

# abrir cada archivo y guardar cada uno en un diccionario o en una lista (según conveniencia)
def cargarDicHabitantes():
    archHab = open("habitantes.txt","r") # abrir archivo
    dicHab={}                            # crear dicionario vacio
    for linea in archHab.readlines():    # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                 # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")           # de string a lista

        # convertir a cada elemento de la lista en su tipo de dato original
        # ya que están asignados como string
        linea[0]=int(linea[0])           # conversión a int
        # la posicion [1] queda como string
        linea[2]=int(linea[2])           # conversión a int
        linea[3]=int(linea[3])           # conversión a int
        dicHab[linea[0]]=[linea[1],linea[2] ,linea[3]] # guardar los elementos leidos en un diccionario
        
    archHab.close()                      # cerrar archivo
    return dicHab                        # retornar el diccionario con los datos del archivo

def cargarListaHabitantes():
    archHab = open("habitantes.txt","r") # abrir archivo
    listaHab=[]                          # crear lista vacia
    for linea in archHab.readlines():    # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                 # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")           # de string a lista

        # convertir a cada elemento de la lista en su tipo de dato original
        # ya que están asignados como string
        linea[0]=int(linea[0])           # conversión a int
        # la posicion  [1] queda como string
        linea[2]=int(linea[2])           # conversión a int
        linea[3]=int(linea[3])           # conversión a int
        listaHab.append (linea)          # guardar la lista "linea" en la lista lisHab (lista de lista)
    
    archHab.close()                      # cerrar archivo
    return listaHab                      # retornar la lista cargada con los datos del archivo


def cargarDicLocalidades():
    archLoc = open("localidades.txt","r")# abrir archivo
    dicLoc={}                            # crear diccionario vacia
    for linea in archLoc.readlines():    # por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                 # eliminar caracter'\n' del final del string de cada linea

        linea=linea.split(",")           # de string a lista
        
        # convertir a cada elemento de la lista en su tipo de dato original
        # dado que están asignados como string
        linea[0]=int(linea[0])           # conversión a int
        # la posicion [1] queda como string
        linea[2]=int(linea[2])           # conversión a int
        
        dicLoc[linea[0]]=[linea[1],linea[2]] # guardar los elementos leidos en un diccionario
    
    archLoc.close()                      # cerrar archivo
    return dicLoc                        # retornar la lista con los datos del archivo

def cargarDicHabXLoc():
    archHabXLoc = open("habitantesXlocalidad.txt","r")# abrir archivo
    dicHabXLoc={}                        # crear diccionario vacia
    for linea in archHabXLoc.readlines():# por cada linea leída del archivo se asigna a la variable línea
        linea=linea[:-1]                 # eliminar caracter'\n' del final del string de cada linea
                                        
        linea=linea.split(",")           # de string a lista

        # convertir a cada elemento de la lista en su tipo de dato original
        # dado que están asignados como string
        linea[0]=int(linea[0])           # conversión a int
        linea[1]=int(linea[1])           # conversión a int

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
    listaCumple=[]                           # lista de los que cumplen la consición buscada en esta funcion
    
    # Buscar el id de la localidad que pertenece al nombre de localidad pasado por parámetro
    # Hay que iterar porque el diccionario tiene como clave el id y no el nombre
    claves=list(dicLoc.keys())
    i=0
    while i<=len(claves)and idLoc==-1:       # iterar el diccionario localidad
        if dicLoc[claves[i]][0]==loc:
            idLoc=claves[i]                  # asignar clave a una variable
        i+=1
    # ACLARACION: Para este caso sería mejor cargar un diccionario con el nombre de la localidad
    # como clave. Pero no se realizó así porque el enunciado indica que la clave es el id
    # (sea único <=> clave)


    if(idLoc!=-1):                           # sólo entrar si encontró un idLoc para la localidad pasada por parámetro
        contHab=0                            # inicializar el contador de habitantes para la condición
        for hab in listaHab:                 # Iterar la lista de habitantes
            valor=dicHabXLoc.get(hab[0])     # Obtener el valor de una clave del diccionario dicHabXLoc
                                             # Si la clave no existe retorna None
                                             # obtener el valor dicHabXLoc[hab[0]] "sin el uso de get", daría error al no encontrar una clave
            if hab[2]==hijos and valor==idLoc:      # Si coincide la cantidad de hijos y tiene el id de localidad (de la localidad pasada por parámetro)...              
                listaCumple.append((hab[0],hab[1])) # Se agregan a la lista aquellos habitantes que cumplen la condición
                                             
    return listaCumple                       # retornar la lista con los elemntos que cumplen la consición

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
    claves=list(dic.keys())                   # obtener una lista con las claves del diccionario dic 
    ordenarLista(claves)                      # ordenar la lista de claves
    print ("{0:15}{1:15}\n".format("Id Localidad","Promedio Edad")) # Imprimir la cabecera de la tabla de salida
    for clave in claves:                      # iterar la lista ordenada de claves del diccionario
        print ("{0:<15}{1:<15}\n".format(clave, dic[clave])) # Imprimir los datos del diccionario

def ordenarLista(lst):                        # ordenar una lista
    for i in range(0,len(lst)-1):
        for j in range(i,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]


def main():
    #--------- INICIO PROGRAMA PRINCIPAL ----------#

    localidad='Lujan'  # asigno para testear
    hijos=3            # asigno para testear

    # Obtener laa lista con los habitantes que cumplen pertenecer a
    # una localidad y tiene una cantidad de hijos
    lstHabHijos = cantHabitantes(localidad,hijos)   
    print ("Lista de  habitantes que tienen {0} hijos en {1}:\n{2}\n".format(hijos,localidad,lstHabHijos)) # Imprimir los datos del diccionario

    edadXLocalidad()

    #---------FIN PROGRAMA PRINCIPAL --------------#

main()                      # llamada a la función principal main(). Como es la unica
                            # llamada a función que está en el cuerpo del archivo 
                            # => es la que se ejecuta
