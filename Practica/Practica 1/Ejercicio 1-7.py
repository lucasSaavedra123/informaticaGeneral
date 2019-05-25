##uso de enteros
numero1 = int(input("Ingresar el primer numero: "))
numero2 = int(input("Ingresar el segundo numero: "))

numero1 = numero1 % 10
numero2 = (int(numero2 / 10) % 10 ) * 10

numero3 = numero1+numero2

print("El numero resultante es: ", numero3)

##uso de caracteres
numero1 = input("Ingresar el primer numero: ")
numero2 = input("Ingresar el segundo numero: ")

numero1 = numero1[len(numero1) - 1]
numero2 = numero2[len(numero2) - 2]

numero3 = int(numero1+numero2)

print("El numero resultante es: ", numero3)