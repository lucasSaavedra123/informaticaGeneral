def agregarDicEle2(i,e,dic):
    dic[i] = e
    return

def imprimirTraduccion(n,idioma,dic):

    if idioma == 'sp':
        print("{} en Español: {}".format(n,dic[n][0]))
    elif idioma == 'en':
        print("{} en Ingles: {}".format(n,dic[n][1]))
    elif idioma == 'en':
        print("{} en Aleman: {}".format(n,dic[n][2]))

    return

def main():

    dic = {}
    numero = int(input("Ingrese un numero (termine con '0' la carga): "))

    while not numero == 0:

        while numero in dic.keys():
            numero = int(input("ERROR! Ya ha ingresado ese numero. Ingrese un numero: "))

        if not numero == 0:
            enEspañol = input("Ingrese el numero en español: ")
            enIngles = input("Ingrese el numero en ingles: ") 
            enAleman = input("Ingrese el numero en aleman: ")

            agregarDicEle2(numero,(enEspañol,enIngles,enAleman),dic)
            print()

            numero = int(input("Ingrese un numero (termine con '0' la carga): "))

    
    numero = int(input("Ingresar nùmero a traducir o cero para salir: "))


    while not numero == 0:

    
        while not numero in dic.keys() and not numero == 0:
            numero = int(input("ERROR! Ingrese un numero (termine con '0' la carga): "))

        if not numero == 0:
            idioma = input("Ingresar idioma ['en'|'sp'|'de']: ")

            while not idioma in ['en','sp','de']:
                idioma = input("ERROR! Ingresar idioma ['en'|'sp'|'de']: ")
            
            imprimirTraduccion(numero,idioma,dic)
            numero = int(input("Ingrese un numero (termine con '0' la carga): "))
        
            
    return


    

main()
