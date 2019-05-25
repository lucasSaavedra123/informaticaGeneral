numero = float(input("Ingresar un numero real: "))

entero  = int(numero) #
decimal = numero - entero

print("Parte entera: ", entero)
print("Parte decimal: ", round(decimal, 3))