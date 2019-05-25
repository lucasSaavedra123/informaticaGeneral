def ingreso():
    
    n = float(input("Ingrese un numero entero: "))
    
    while not n - int(n) == 0:
        n = float(input("Error! Ingrese numero entero: "))
        
    return n

def main():

    contador = 0

    while contador < 5:
        
        numero = ingreso()
                
        if numero % 2 == 0 and numero % 4 == 0:
            contador = contador + 1
            print("Numero Par. Tambien es multiplo de 4. Total de numeros pares ingresados: {}".format(contador))
            
        elif numero % 2 == 0:
            contador = contador + 1
            print("Numero Par. Total de numeros pares ingresados: {}".format(contador))

    print("FIN")
    
    return 0



main()