numero_decimal = int(input("Ingrese un numero decimal (maximo 5 cifras): "))

numero_octal = numero_decimal % 8 

numero_decimal = numero_decimal // 8
numero_octal = ( numero_decimal % 8 ) * 10 + numero_octal

numero_decimal = numero_decimal // 8
numero_octal = ( numero_decimal % 8 ) * 100 + numero_octal

numero_decimal = numero_decimal // 8
numero_octal = ( numero_decimal % 8 ) * 1000 + numero_octal

numero_decimal = numero_decimal // 8
numero_octal = ( numero_decimal % 8 ) * 10000 + numero_octal

numero_decimal = numero_decimal // 8
numero_octal = ( numero_decimal % 8 ) * 100000 + numero_octal


print("Numero en octal: ", numero_octal)