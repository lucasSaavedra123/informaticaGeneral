def justificado(fra, ancho):
    print("'{:>{a}}'".format(fra, a = ancho))
    return

def main():
    frase = input("Ingrese la frase: ")
    ancho = int(input("Ingrese el ancho total a ser usado: "))
    justificado(frase, ancho)
    return

main()