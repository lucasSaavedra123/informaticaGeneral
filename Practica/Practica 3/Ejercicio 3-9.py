def bono(sb):
    
    if sb > 2000:
        return sb * 0.15
    else:
        return sb * 0.20

def plusH(sb, h):
    
    if h.lower() == "s":
        return sb * 0.05
    else:
        return 0
    
def plusC(sb, c):
    
    if 1 <= c <= 3:
        return sb * 0.1
    
    elif 4 <= c <= 6:
        return sb * 0.12
    
    elif 7 <= c <= 9:
        return sb * 0.2

def main():

    sueldoBase = int(input("Ingrese el sueldo base ($): "))
    hijos = input("¿Tiene hijos? (s/n): ")
    categoria = int(input("Ingrese categoria ( 1 - 9 ): "))

    if 7 <= categoria <= 9:
        sueldoTotal = sueldoBase + bono(sueldoBase) + plusC(sueldoBase, categoria)
    else:
        sueldoTotal = sueldoBase + bono(sueldoBase) + plusH(sueldoBase, hijos) + plusC(sueldoBase, categoria)


    print("El sueldo total será de ${}".format(sueldoTotal))
    
    return

main()

