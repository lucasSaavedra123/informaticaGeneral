##Ejercicio 1.1
def ingresar():
    n=int(input())
    while not(n%3==0 and not n%7==0 and not n%2 == 0):
        print('Error')
        n = int(input())
    return n

##Ejercicio 1.2
def foo1(A,B):
    lst = []
    
    for i in A:
        if not i in B and not i in lst:
            lst.append(i)
    
    for i in B:
        if not i in A and not i in lst:
            lst.append(i)

    return lst



##Ejercicio 2.1. Respuesta: e
def foo2(miStr,num):
    miStr[num]='x'
    y=num-1
    return miStr[num-y]

##Ejercicio 2.2. Respuesta:
import random
def aleatorio():
    lst = []
    for i in range(0,5):
        x = (random.randint(0,20)%5)*2
        lst.append(x)
    return lst


##Ejercicio 2.3. Respuesta: e
def punto23():
    lst = [10,20,30,40,50]
    tam = len(lst)
    i=1
    suma=0
    while i <= tam:
        suma+=lst[i]
        i+=1
    print(suma)
    return


##Ejercicio 2.4. Respuesta: b
def foo3():
    sum = '0'
    for x in '0123':
        if not(x=='0' and x=='1')==(not x=='0' or not x=='1'):
            sum=sum+x
    return sum
    

def main():
    return

main()

