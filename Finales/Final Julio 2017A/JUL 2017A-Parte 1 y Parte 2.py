##Ejercicio 1.1.
def ordenar(A):
    i=0;j=0;aux=0
    
    while i<len(A):
        j=0
        while j<len(A):
            if A[i]<A[j]:
                aux=A[i]
                A[i]=A[j]
                A[j]=aux
            j+=1
        i+=1
    
##Ejercicio 1.2.
def foo(n):
    for i in range(1,n):
        if i%2 == 0:##Pregunta si es par
            salida='x'
        else:
            salida = 'y'
        print(salida*i,end="")
        

##Ejercicio 2.1. Respuesta: d
def punto21():
    x=2
    cc = ['2','4','3']
    y = cc[0] * x**0 + cc[1] * x**1 + cc[2] * x**2
    print(y)
    return


##Ejercicio 2.2. Respuesta:d
def foo2(A,B):
    lst = [] + A
    for x in B:
        if x not in A:
            lst.append(x)
        else:
            lst.remove(x)
    return lst

def punto22():
    print(1,foo2([2,3,11,10],[11,102,3,2]))
    return


##Ejercicio 2.3. Respuesta: a
def foo3(lst):
    for j in range(len(lst)-1,0,-1):
        for i in range(j):
            if lst[i]<lst[i+1]:
                temp = lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=temp

def punto23():
    lista = [14,46,21,18]
    foo3(lista)
    print(lista)
    return

##Ejercicio 2.4. Respuesta:f
def foo4(miS):
    sum=0
    for x in miS:
        sum = sum+miS[x]
    print(sum)
    return

def punto24():
    
    numS = '0123'
    foo4(numS)
    
    return


def main():
    punto24()
    return

main()