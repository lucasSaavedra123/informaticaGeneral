def validacion(n):

    while n < 0 or n - int(n) != 0:
        n = float(input("ERROR! Ingrese solamente numeros NATURALES: "))
    
    return n

def listaDePrimos1(cant):

    print("\n\n\nPrimos entre 1 y {}:".format(cant))

    """SE IMPRIMEN TODOS LOS NUMEROS PRIMOS HASTA CANT"""

    a = 1
    
    for indice in range(1, cant):

        cantidadDivisibles = 0
        contador = 1
        
        while (contador <= indice):

            if indice % contador == 0:
                cantidadDivisibles = cantidadDivisibles + 1
                
            contador = contador + 1

        if cantidadDivisibles == 2:
            
                print("\t{}".format(indice), end = " ")

                if a == 10:
                    print("\n")
                    a = 1
                else:
                    a = a + 1 

    return

def listaDePrimos2(cant):


    print("\n\n\nPrimeros {} primos:".format(cant))

    """SE IMPRIMEN LOS PRIMEROS CANT PRIMOS"""
    a = 1
    indice = 0
    cantidadDePrimos = 0
    
    while cantidadDePrimos < cant:

        cantidadDivisibles = 0
        contador = 1
        
        while (contador <= indice):

            if indice % contador == 0:
                cantidadDivisibles = cantidadDivisibles + 1
                
            contador = contador + 1

        if cantidadDivisibles == 2:

            print("\t{}".format(indice), end = " ")

            if a == 10:
                print("\n")
                a = 1
            else:
                a = a + 1 

            cantidadDePrimos = cantidadDePrimos + 1

        indice = indice + 1
    
    return

def main():
    
    cant = int(input("Ingrese cantidad (numero natural) :"))
    cant = validacion(cant)

    listaDePrimos1(cant)
    listaDePrimos2(cant)
    
    return

main()