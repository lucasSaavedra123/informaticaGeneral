def esLetra(l):
    return "a" <= l <="z" or "A" <= l <="Z" or l in "áéíóúÁÉÍÓÚ" 


def extraerCaracter(letra):
    
            if 'A' <= letra <= 'Z':
                return chr( ord(letra) + 32 )
            elif  letra in "áéíóúÁÉÍÓÚ":
                
                if letra in "áÁ":
                    return "a"
                elif letra in "éÉ":
                    return "e"
                elif letra in "ií":
                    return "i"
                elif letra in "óÓ":
                    return "o"
                elif letra in "úÚ":
                    return "u"
            else:
                return letra


def esPalindroma(texto):
    
    texto1 = ''
    i = 0
    
    while i < len(texto):
        
        if esLetra(texto[i]):
            texto1 = texto1 +  texto[i]
            
        i += 1
    
    texto2 = texto1[::-1]
    
    i = 0
    
    while i < len(texto1):
        
        if not ( extraerCaracter(texto1[i]) == extraerCaracter(texto2[i]) ):
            return False
        
        i += 1
    
    return True



def main():
    
    texto = input("ingrese una frase: ")
    
    if esPalindroma(texto):
        print("La frase es palindroma!")
    else:
        print("La frase no es palindroma!")
    
    return
    
main()