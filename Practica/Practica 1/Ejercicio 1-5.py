numero = int(input("Ingrese un numero de 5 digitos: "))

numero1 = ( numero % 10 ) ** 2

numero  = int(numero / 10)
numero2 = int( numero % 10 ) ** 2

numero  = int(numero) / 10
numero3 = int( numero % 10 ) ** 2

numero  = int(numero) / 10
numero4 = int( numero % 10 ) ** 2

numero  = int(numero) / 10
numero5 = int( numero % 10 ) ** 2


print("-",numero1,"-",numero2,"-",numero3,"-",numero4,"-",numero5)