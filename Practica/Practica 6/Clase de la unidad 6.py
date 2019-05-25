"""

Estructura de datos: Colecciones (se usa para dar informacion de individuo, persona, animal como la edad, peso, etc)
Sirven para juntar un determinado conjunto de valores
Hay tres conceptos, tres formas.

Dupla es el nombre generico que se le da a la matematica para decir que algo tiene dos elementos
Tupla es para algo que tiene dos o mas elementos
Se describen utilizando ',' para representar cada elemento del Tupla

COSAS DE STRINGS SE PUEDEN USAR EN TUPLAS

SE PUEDEN HACER TUPLAS DE TUPLAS Y LISTAS DE LISTAS

"""

##Los parentesis son optativos. El coma define a la tupla
punto = 2, 5
punto3D = (5 , 1 , -1.3)
print(punto)
print(punto3D)
##Se pueden dar tuplas vacias
t1 = ()
print(t1)
##O de un solo elemento
t1 = (1)
print(t1)
##Se se quiere imprimir con parentesis
t1 = (1,)
print(t1)
##No se puede poner t1(,)
##Los parentesis siguen siendo optativos
##Los valores de la tupla no pueden cambiar, son inmutables
##Se le puede dar valores a la tupla, haciendo:
a,b=input("A: "),input("B: ")
##Se puede hacer de otra manera
##Estas son rarezas de la tuplas, luego vamos a ver
##como realmente se usan
##Para intercambiar valores se puede hacer
a=0 ##Debuggear estos pasos
b=5
b,a=a,b
##Se pueden mezclar tipos de datos
t1 = ('a',5)
print(t1)

##Se usan las tuplas para poder representar los datos de un inviduo real en una sola variable
##Por ejemplo

persona1 = ('Lucas', 'Saavedra',19,1.67,76.2)##Estos datos no se pueden cambiar

##Para acceder al valor de la tupla se usan []. AL igual que en los strings.
##Se lo puede usar como un slic e

persona1[1:2]

nombreDePersona = persona1[0]
print(nombreDePersona)

##Sumar tuplas genera una tercera tupla

a=(1,3)
b=(2,9)
c = a + b

##Multiplicar tambien

c = a * 2

##Se lo puedo usar para poder hacer que una funcion devuelva dos valores

def divResto(d,c):
    return d//c,d%c

cociente,resto=divResto(67,4)

"""
Recien vimos tupla.

Hay otra estructura de datos que es la mas flexible de todas y es la mas util.
Esta estructura la vamos a usar para presentar coleccion o grupo de elementos.
Esta estructura es 'lista'.

Son MUTABLES, SI SE PUEDEN CAMBIAR

ES PREFERIBLE QUE EN UN PROGRAMA HAYA ELEMENTOS MUTABLES
"""
##Para representar listas usamos corchetes para poder representar el conjunto de elementos

lista = [3,1,5,6,4,7,8]
print(lista)

listaNula = []
print(listaNula)

listaUnica = [5]
print(listaUnica)

##Dada una lista se puede cambiar el valor de uno de los que conforma a la lista

lista = [3,5,6,9,8]
lista[2] = 3
print(lista)

lista[1:4] =[0,0,0]
print(lista)

##Las listas se puede conectar por medio de la asignacion con otra variable
##Ver que no pasa lo mismo con los strings ya que no se puede cambiar
##Ni tampoco como las variables

lista1 = [1,2,5,4,8]
lista2 = lista1
lista2[2]=100000 ##Sigue siendo lista1. Es otro nombre que se le puede dar a una lista. No es otra lista
print(lista1)

##Con las funciones pasa algo parecido

def modificar(l):
    l[0] = 999
    
modificar(lista1)
print(lista1)

##Se puede probar lo siguiente

lista1 = [4,5,6,7,8,9,10,12,45]
lista3 = lista[3:]##Se crea otra lista diferente. Ya no esta conectado con lista1
lista3[0] = 100
print(lista1)
print(lista3)

###Listas en listas puede servir para poder hacer filas y columnas

matriz=[[1,2,3],
        [5,6,3],
        [0,1,0]]

print(matriz)

##Con un for podemos imprimirlo como una matriz
print()

for f in matriz:
    for c in f:
        print(c, end = " ")
    
    print()
    
    
##Con el 'in' se puede ver si uno de los elementos esta en la lista

if 5 in [1,2,3,6,5]:
    print("Es verdadero")
else:
    print("No es verdadero")
    
##Si queres agregar valores a la lista usamos el append()
    
lista = [1,2,3,6] + [4] ##o podemos usar el append
lista.append(4)##Le agregar un espacio mas a la lista. SE PUEDE USAR

##Se va a imprimir con dos 4 al final
print(lista)

##Si queres insertar un valor en una cierta posicion usamos insert

lista.insert(2, 'so vo')##Posicion, valor a agregar ##Queda una lista mas larga
print(lista)
##Si ponemos insert 0 se pone al principio


##Otra funcion es pop. Elimina el ultimo valor de la lista y lo retorna.
print(lista)
print(lista.pop())
print(lista)

##Para borrar algo de una lista hay dos manera:
##Una es con remove(). 

lista.remove(4)##Se le da valores. SI ese valor esta en la lista, lo borra.##Se basa en una valor
print(lista)

##Primero hay que ver si esta en la lista
##Si no se pregunta, y ese valor no esta, sale error

if 0 in lista:
    lista.remove(0)#

##Si queremos borrar tmbien se puede usar 'del'
    
del lista[2] ##Se basa en una posicion
print(lista)

##Se pueden poner tuplas adentro de listas

lista = [("Juan", "Martin") , ("Horacio" , "Gonzalez")]
print(lista)
lista[0] = ("Martin","Caudal")
print(lista)
lista.append(("Nombre", "apellido"))
print(lista)

##Se pueden ir tomando valores en forma de 'cola' con append
##En la cola, el orden en que entran es igual a como salen (el primer que entro sale primero) Se hacen con un insert(0,)
##En forma de pila, el orden en que entras es inverso a como salen (el primero que entro, sale ultimo (en .pop se refleja eso)
##Se usa con append para poner y para sacar pop()
##Pila y Cola son estructuras de cola

""" Otra forma de representar coleccion de datos son los diccionarios
tiene la particularidad de ser listas donde el indice [] no necesariamente es numérico
Como indice podriamos usar una palabra

Se pueden usar como para buscar cosas rapido
y son mutables
"""

##Se representan entre llaves

dic = {}##Diccionario
print(dic)

dic = {"Hola"}
print("Hola")

##Puede resultar hacer muchas cosas de una manera mas rapida
##Por ejemplo, dar las capitales de los paises.
##Le pedis que elemento tiene asignado el dato que le das, y te lo da

##Se guarda de esta manera:

"""
diccionario = {"nombre del indice":"valor asignado",...,...}
"""

##Entonces:

dic = {'Argentina':'Buenos Aires', 'Uruguay':'Montevideo'}
print(dic['Argentina'])
"""NOTA: Cualquier cosa puede ser un indice y cualquier cosa puede ser un valor"""


##Si queremos agregar valores al diccionarios se pone:

dic[0]="So vo"##En el indice ya se le pone su nombre
dic['Japon']='Tokio'
print(dic)

##Remove no se puede usar en dic (lo podriamos crear) pero si se puede usar 'del'

del dic [0]
print(dic)

##Una manera de ver el valor de un indice es
dic.get('Argentina')
##Si no esta el indice que le damos, no pasa nada.
##Esa es la diferencia con usar corchetes

##Si queremos saber que indices hay

indices = dic.keys()
print(indices)

##Si queremos saber todos los valores de cada indice

valores = dic.values()
print(valores)

##Estos devuelven otro tipo de dato, no son listas, ni tuplas.
##Se guarda en colecciones llamadas dict_keys o dict_values
##pero se lo puede usar en un for

for ciudad in dic.values():
    print(ciudad)

##NUNCA AGREGUEN O BORREN ELEMENTOS A UNA LISTA O UN DICCIONARIO,
##CUANDO ESTAN RECORRIENDO (CON UN FOR ... IN ...)

#y podriamos convertir eso lista usando list()

lista = list(dic.values())
print(lista)

#Tmb se lo puede usar para strings o tuples

cadena = 'hola'
lista = list(cadena)
print(lista)



##BREAK corta cualquier ciclo de repeticion. En un for o while etc.

##Si queremos hacer una copia de un diccionario o lista etc.
##se puede usar el copy()


"""En todas las colecciones no se manejan como variables (en tuplas y strings no, ya que no son mutables)
lista = [1]
lista2 = lista ##Lista2 es otro nombre para lista
##es como se crea una flecha
##en el pasaje de parametros es igual
##si modifico lista2, modifico lista

si luego hacemos lista2 = {}, perdemos la conexion con lista



"""