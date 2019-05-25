def digitSum (number):

    sum = number % 10
    sum = sum + (number // 10) % 10
    sum = sum + (number // 100) % 10
    sum = sum + (number // 1000) % 10
    sum = sum + (number // 10000) % 10
    sum = sum + (number // 100000) % 10
    sum = sum + (number // 1000000) % 10
    sum = sum + (number // 10000000) % 10
    
    return sum
    

def paridad(b):
    
    suma = digitSum(b)
    bit = suma % 2
    
    return bit

def main():
    numeroBinario = int(input("Ingrese un numero binario de hasta 8 bits: "))
    print("Bit de paridad generado: ", paridad(numeroBinario))

    return

main()