def compositor(e,p):    
    return e[0] + p + e[1]


def main():
    
    extremos = input("Ingrese los extremos: ")
    palabra = input("Ingrese palabra: ")
    
    if len(palabra) == 0 or len(extremos) != 2:
        print("\nLa función ha retornado una palabra vacía.")
    else:
        print("\nLa función retornó: {}".format(compositor(extremos, palabra)))
    
    return

main()