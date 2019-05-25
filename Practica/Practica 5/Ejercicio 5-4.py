def principioFin(s):

    if len(s) == 1:
        return True

    i = 0
    iPrincipal = 0 ##Se toma la posicion donde arranca una letra
    iFinal = 0 ##Se toma la posicion de la ultima letra

    while not ("a"<= s[i] <= "z" or "A" <= s[i] <= "Z" or s[i] in "ÁÉÍÓÚáéíóú"):
        iPrincipal += 1
        i += 1

    i = 0

    while not ("a"<= s[- 1 - i] <= "z" or "A" <= s[- 1 - i] <= "Z" or s[- 1 - i] in "ÁÉÍÓÚáéíóú"):
        iFinal -= 1
        i += 1

    i = 0
    palabra1 = ''
    palabra2 = ''
    
    while ( 'a' <= s[iPrincipal + i] <= 'z' or 'A' <= s[iPrincipal + i] < 'Z' or s[iPrincipal + i] in 'ÁÉÍÓÚáéíóú' ) and ( 'a' <= s[iFinal - i - 1] <= 'z' or 'A' <= s[iFinal - i - 1] <= 'Z' or s[iFinal - i - 1] in 'ÁÉÍÓÚáéíóú' ):
        palabra1 =  palabra1 + s[iPrincipal + i]
        palabra2 =  s[iFinal - i - 1] + palabra2
        i += 1


    if not (s[iPrincipal + i] == ' ' and s[iFinal - i - 1] == ' '):
        return False

    i = 0


    while not ( i < len(palabra1) or i < len(palabra2) ):

        if "A" <= palabra1[i] <= "Z":
            caracter1 = chr( ord(palabra1[i]) + 32 )
        elif palabra1[i] in "ÁÉÍÓÚ":
            
            if palabra1[i] == "Á":
                caracter1 = "á"
            if palabra1[i] == "É":
                caracter1 = "é"
            if palabra1[i] == "Í":
                caracter1 = "í"
            if palabra1[i] == "Ó":
                caracter1 = "ó"
            if palabra1[i] == "ú":
                caracter1 = "ú"
        else:
            caracter1 = palabra1[i]

        if "A" < palabra2[i] < "Z":
            caracter2 = chr( ord(palabra2[i]) + 32 )
        
        elif palabra2[i] in "ÁÉÍÓÚ":
            
            if palabra2[i] == "Á":
                caracter2 = "á"
            if palabra2[i] == "É":
                caracter2 = "é"
            if palabra2[i] == "Í":
                caracter2 = "í"
            if palabra2[i] == "Ó":
                caracter2 = "ó"
            if palabra2[i] == "ú":
                caracter2 = "ú"
                
        else:
            caracter2 = palabra2[i]

        if not caracter1 == caracter2:
            return False
        
        i += 1
    
    return True

def main ():
    
    palabra = input("Ingrese un texto: ")
    
    if principioFin(palabra):
        print("El texto cumple la condicion")
    else:
        print("El texto no cumple la condicion")
    
    return

main()
