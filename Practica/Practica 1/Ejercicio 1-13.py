multiplicando = int(input("Ingresar el multiplicando de 3 cifras: "))
multiplicador = int(input("Ingresar el multiplicador de 3 cifras: "))

numero1 = (multiplicador % 10) * multiplicando
numero2 = (int(multiplicador/10) % 10)  * multiplicando
numero3 = (int(multiplicador/100) % 10) * multiplicando

resultado = multiplicando * multiplicador
   
print(" ")
print("{:>10}".format(multiplicando))
print("x{:>9}".format(multiplicador))
print("{:-<10}".format(""))#Tambien podemos poner print("-" * 10) Se imprime la linea

print("{:>10}".format(numero1))
print("+{:>8}-".format(numero2))
print("{:>8}--".format(numero3))

print("{:-<10}".format(""))
print("{:>10}".format(resultado))
