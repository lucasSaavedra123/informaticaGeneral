##Ejercicio 1.1.
def ordenArr(A):
    for i in (range(len(A))):
        for j in (range(len(A))):
            if (A[i]<A[j]):
                A[i],A[j]=A[j],A[i]
    return

##Ejercicio 1.2.
def decAbin(num):
    resto=0
    i=0
    bina=0
    while(num>0):
        resto=num%2
        num=num//2
        bina=bina+resto*(10**i)
        i=i+1
    
    return bina

##Ejercicio 2.1. Respuesta: c
def fa(a):
    return fb(a)+1

def fb(b):
    for i in range(0,len(b)):
        return int(''.join(b))+i

def punto21():
    a = ['1','2']
    print('{0:d}{1:d}'.format(fb(a),fa(a)))
    return


##Ejercicio 2.2. Respuesta: d
def comparar(a,b,c):
    if((a and (b or c))==((a and b)or(a and c))):
        return True
    else:
        return False

def punto22():
    print("{0:d}{0:d}".format(0,comparar(1,1,1)))
    return


##Ejercicio 2.3. Respuesta: e (no imprime nada)
def f1(x):
    for i in range(0,len(x)):
        if i in x:
            print('a',end='')
        else:
            print('b',end='')

def punto23():
    x=list(range(10,1,2))
    f1(x)
    return

##Ejercicio 2.4. Respuesta:e
def punto24():
    s=['Juan','Carlos']
    s='Carlos'
    s='Juan'
    s[0]='x'
    print(s)
    return


def main():
    punto24()
    return

main()