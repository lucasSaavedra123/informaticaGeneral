def main():
    
    ##Strings: Cadena de caracteres (palabras, etc)
    ##Se representan con comillas (simples o dobles).
    ##Se crean cada vez que se pone algo entre comillas,
    ##cada vez que se usa un slice ([:], mas adelante esta),
    ##y cada vez que se usa el "+" y el "*" con un string
    
    string = 'hola'
    string = "hola"
    
    ##Es lo mismo
    ##Si se quiere hacer una cita:
    
    string = "Yo dije 'hola' y se fue" ##Se imprime con comilla simple
    print(string)
    
    string = 'Yo dije "hola" y se fue' ##Se imprime con comilla doble
    print(string)
    
    ##Si se quiere poner "..." para escribir y adentro se quiere citar con
    ##"..." entonces:
    
    string = "Se llama Pedro, pero le dicen \"Pepe\" "
    print(string)
    
    
    ##Concatenar (uso de operando con) strings
    ##Se se quiere unir cadenas se puede hacer:
    
    a = "Hola"
    b = "Mundo"
    
    string = a + " " + b
    
    print(string)
    
    ##El operado asterico espera a que uno de los operando sea un numero.
    ##Si se quiere operar con dos string, no se puede.
    
    a = "Hola"
    string = a * 5
    
    print(string)
    
    ##Condicionales con String
    ##Si se quiere saber si una letra esta en la cadena, se puede usar:
    
    print("b" in "hola") ##Falso por que 'b' no esta en 'hola'
    print("a" in "hola") ##Verdadero por que 'a' esta en 'hola'
    
    ##El String es una lista de letras y el 'in' trabaja con listas.
    ##Si se usa mas de una letra
    
    print("la" in "hola") ##Verdadero por que 'la' aparece en la lista de manera secuencial
    print("al" in "hola") ##Falso por que 'al' no aparece en la lista de manera secuencial
    
    ##Este condicional se lo podria usar para poder buscar palabras en un texto
    
    ##LAS FUNCIONES QUE SE USAN PARA LOS STRINGS
    ##variable.capitalize() se usa para poner la primera letra de una palabra
    ##en mayuscula
    
    string = "hola"
    print(string.capitalize())
    
    ##esta funcion no se puede usar.
    ##Las que se pueden usar es format (ya la vimos) y len().
    ##Esta ultima funcion da el ancho de un string
    
    string = "hola"
    print( len(string) )
    
    ##INDICE
    ##Se pueden acceder a los elementos de la cadena por medio de los indices
    
    string = "hola"
    print(string[0])
    print(string[3])
    
    ##Es una posicion de la cadena y se empieza a contar desde 0.
    ##Por ejemplo, si se quiere conseguir el ultimo numero de una cadena, se hace:
    
    string = "hola"
    print(string[len(string) - 1])
    
    ##Se puede usar el indice -1. Aca se va de derecha a izquierda
    
    string = "hola"
    print(string[-1])
    print(string[-2])
    
    ##Si se quiere tomar un pedazo del string
    
    string = "hola"
    print( string[0:2] )

    ##El primer numero es el primer indice por el cual se empieza y
    ##y el ultimo es el ultimo indice no inclusive. En este caso
    ##coincide con la cantidad de letras a imprimir.
    ##Siempre la cantidad termina siendo (ultimo numero - primer numero)
    
    string = "hola mundo!"
    print( string[1:-1] )
    print( string[1:10] )
    
    ##Si no se lo pone en orden entrga una cadena vacia
    
    ##Si no se ingresan numero:
    
    string = "hola mundo!"
    print ( string[:] )
    
    ##Si se agrega otro valor, se considera que es un salto
    
    string = "hola mundo!"
    print( string[1:4:2] )
    print( string[-1:-4:-1] ) ##Si el salto es negativo, va para atras
    
    ##Si se quiere invertir un string se puede usar:
    
    string = "hola mundo!"
    print( string[::-1] ) ##Va de principio hasta fin y de manera inversa.
                          ##Ya que el salto es negativo    
    
    
    ##Los strings son inmutables, no se puede cambiar.
    ##No se puede cambiar una letra de la cadena
    
    
    ##Codigo ASCII
    ##Para saber el codigo ASCII de un caracter se hace ord(caracter) y te da el numero correspondiente
    ##Para saber el caracter por medio del codigo se hace chr(numero) y nos dara el caracter correspondiente
    
    
    ##HASTA ACA ENTRA UNIDAD 5
    
    
    ##Si queres tomar palabras hacemos asi:
    ##Sirve para varios ejercicios
    
def esLetra(l):
    return ( 'a' <= l <= 'z' ) or ( 'A' <= l <= 'Z' ) or l in 'áéíóúÁÉÍÓÚ'

def procesar(texto):
        
    i = 0
        
    while i<len(texto):
        
        while i<len(texto) and not esLetra(texto[i]):
            i += 1
        
        comienzo = i
        
        while i<len(texto) and esLetra(texto[i]):
            i += 1
        
        final = i-1
        
        
        if comienzo <= final: ##Lo ponemos por si hay doble o mas espacios o doble o mas simbolos no aceptados
            print(texto[comienzo:(final+1)] + "\t", end = "")

    return

        ##Si queres modificar una cadena (directamente no se puede):
def modificar(palabra, pos, letra):
    return palabra[:pos] + letra + palabra[pos+1:]

        ##SI queremos sabes si es minuscula y queres pasarlo a mayuscula

def aMayuscula(l):
    if l >= "a" and l <= "A":
        return chr( ord(l) - (ord("a") - ord("A")))
    else:
        return l

def main():
    
    print(modificar("hola", 2, "0"))

main()



    ##Si queremos ordenar

def intercambiar(palabra, pos1, pos2): ##Intercambia una posicion el caracter por las posiciones dadas
    return palabra[:pos1] + palabra[pos2] + palabra[pos1+1:pos2] + palabra[pos1] + palabra[pos2+1:]

def ordenar(texto):
    for i in range(len(txt)-1): ##No se toma la ultima por que queremos comparar la ultima despues por que sino no habra
                                ## mas nada para comparar
        for j in range(i+1, len(txt)): ##Se compara una con otra texto[i] y texto[j]
            
            if txt[i] > txt[j]:
                txt = intercambiar(txt,i,j)
            
            
        
        
    
    