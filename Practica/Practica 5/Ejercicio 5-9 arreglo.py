def cumpleCondicion(n):
    
    i = 0
    suma = 0
    producto = 1
    contador = 0
    
    while not n == 0:
        
        c = n % 10
        
        if c == 5:
            return False
        elif c == 7:
            contador += 1
        
        suma = c+suma
        producto = c*producto
        
        n = n // 10
        
    if contador != 0 and suma == producto:
        print(True)
        return True
    else:
        print(False)
        return False
        
def validacion(n):
    while n-int(n) != 0 or n < 0:
        n = int(input("ERROR: "))
    
    return n

def main():
    
    contador = 0
    n = int(input("Ingrese"))
    n = validacion(n)
    
    while not n == 0:
        
        if cumpleCondicion(n):
            contador +=1
        
        n = int(input())
        n = validacion(n)
        
    print("{}".format(contador))
    
    
    
    
main()