##Ejercicio 1.1
def esPrimo(n):##Pasale un entero y probalo llamando en el main()
    primo=True
    i=2
    while (i<n):
        if n%i == 0:
            primo = False
        i+=1
            
    return primo

##Ejercicio 1.2
def espalindromo(texto):
    palindromo = True
    for i in range(len(texto)):
        if(texto[-i-1]!=texto[i]):
            palindromo = False
    
    return palindromo

##Ejercicio 2.1. Respuesta: f (sale error)
def punto21():
    xs=['Hola','Mundo']
    xs = 'Hola'
    xs = 'Mundo'
    xs[0]='x'
    print(xs)
    return

##Ejercicio 2.2. Respuesta:  a
def comparar(a,b,c):
    if (a and (b or c)) != ((a and b) or (a and c)):
        return True
    else:
        return False

##Ejercicio 2.3. Respuesta: d
def f2(x):
    x=x+10
    return x

def f1():
    x=10
    print(str(f2(x))+'-',end='')

def punto23():
    x=5
    f1()
    print("{0:d}".format(f2(x)))
    return

##Ejercicio 2.4. Respuesta: f (sale error)
def punto24():
    xn = [1,2,3,4]
    n=1234
    print((2 in xn) and (2 in n))
    return


def main():
    punto24()
    return

main()