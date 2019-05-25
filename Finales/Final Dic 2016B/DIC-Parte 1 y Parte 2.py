##Ejercicio 1.1
def promlst(lst):
    i=0
    prom=[]
    for sl in range(len(lst)):
        sum = 0
        for i in range(len(lst[sl])):
            sum = sum + lst[sl][i]
        prom.append(sum/(i+1))
    return prom

##Ejercicio 1.2
def ingresar():   
    n = int(input())
    while n%2 == 0 or n%3 != 0 or n%7 == 0:
        print('Error')
        n = int(input())
    return n

##Ejercicio 2.1. Respuesta: b
def punto21():
    x = input()
    if x>='0' or x<='9':
        print('Correcto')
    else:
        print('Incorrecto')

    return

##Ejercicio 2.2. Respuesta: g
def f2(x):
    x-=5
    print(x,'',end='')

def f1():
    x=5
    f2(x)
    print(x,'',end='')

def punto22():
    
    x=1
    f1()
    print(x,'',end='')
    
    return

##Ejercicio 2.3. Respuesta: f
def cambiar(miStr,num):
    miStr[num]='x'
    y=num
    num+=4
    return miStr[num-y]

def punto23():
    cad = 'abcd'
    n=3
    letra = cambiar(cad,3)
    print("{:s}-{:s}-{:d}".format(cad,letra,n))
    ##Si se le pone {:s} toma el formato como si fuese un string. No funciona con enteros ni con float
    return

##Ejercicio 2.4. Respuesta: c
def punto24():
    xn = ['1','2','3','4']
    n = "1234".split()
    a = ('1' in xn)
    b = ('2' in n)
    print(a,b)
    return

def main():
    punto23()
    return

main()