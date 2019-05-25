def extractor(p):
    return p[len(p)-2] + p[len(p)-1]

def main():
    
    palabra = input("Ingrese una palabra: ")
    
    if len(palabra) < 2:
        print("La función ha retornado una palabra vacía.")
    else:
        print("La función ha retornado: {}".format( extractor(palabra) * 3 ))
    
    return

main()
