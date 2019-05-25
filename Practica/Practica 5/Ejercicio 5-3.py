def validarPalabra(s):
    
    for caracter in range(len(s)):
        
        if not ("a" <= s[caracter] <= "z" or "A" <= s[caracter] <= "Z"):
            return True
    
    
    return False


def validacion(s):
    
    while validarPalabra(s) or len(s) % 2 == 1: 
        s = input("Error. Ingrese una palabra de longitud par: ")
        
    return s

def primeraMitad(s):
    return s[ 0 : (len(s)//2) ]

def main():
    
    palabra = input("Ingrese una palabra de longitud par:")
    palabra = validacion(palabra)
    
    print("La funcion ha retornado: {}".format(primeraMitad(palabra))) 
    
    return

main()