"""Uso de string pero no es lo optimo
numero_binario = str(int(input("Ingrese un numero binario de hasta 5 bits: ")) + 100000)

numero_decimal = int(numero_binario[5]) * 1
numero_decimal = numero_decimal + int(numero_binario[4]) * 2
numero_decimal = numero_decimal + int(numero_binario[3]) * 4
numero_decimal = numero_decimal + int(numero_binario[2]) * 8
numero_decimal = numero_decimal + int(numero_binario[1]) * 16
"""
numeroBinario = int(input("Ingrese un numero binario de hasta 5 bits: "))

numeroDecimal =  numeroBinario % 10 * 1
numeroDecimal = (numeroBinario // 10)   % 10 * 2  + numeroDecimal
numeroDecimal = (numeroBinario // 100)  % 10 * 4  + numeroDecimal
numeroDecimal = (numeroBinario // 1000) % 10 * 8  + numeroDecimal
numeroDecimal = (numeroBinario // 10000)% 10 * 16 + numeroDecimal

print("Numero en decimal: ",numeroDecimal)