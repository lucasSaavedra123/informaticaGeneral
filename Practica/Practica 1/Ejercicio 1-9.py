numero = input("Ingrese numero de cantidad impar de cifras (al menos 3 cifras): ")

cifras = len(numero)
numero1 = numero[0]
numero2 = numero[len(numero) - 1]
numero3 = numero[len(numero) // 2]

print("El numero ingresado tiene ", cifras, " cifras")
print("La primera cifra es ",numero1,", la ultima es ",numero3," y la central es ", numero2, ".")