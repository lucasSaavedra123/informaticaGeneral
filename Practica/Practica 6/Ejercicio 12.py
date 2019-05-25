def operaciones(a,b):
    return (a+b,a-b,a*b,a//b)

def main():
    
    a = 18
    b = 5
    
    tupla = operaciones(a,b)
    
    print(tupla)
    ##tupla[0]=0 No se puede
    
    ##Se convierte tupla a lista
    tupla = list(tupla)
    print(tupla)
    
    tupla[0] = 0 ##Se puede
    print(tupla)
    
    
    return

main()