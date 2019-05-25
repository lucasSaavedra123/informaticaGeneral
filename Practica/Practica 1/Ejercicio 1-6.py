base = float(input("Ingresar la base: "))
altura = float(input("Ingresar la altura: "))

area = (base * altura) / 2
perimetro = base + altura + (base**2+altura**2) ** (1/2)

print("Calculos para un triangulo de base ", round(base, 2), "y altura ", round(altura, 2), ":")
print("<<< Area: ", round(area, 2), ">>>            <<< Perimetro: ", round(perimetro, 2), ">>> ")