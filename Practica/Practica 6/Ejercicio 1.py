def estaEnLista1(num,lst):
    
    if num in lst:
        return True
    else:
        return False

def estaEnLista2(num,lst):
    
    for i in lst:
        if i==num:
            return True
    
    return False

def estaEnLista3(num,lst):
    
    i = 0
    
    while i < len(lst):
        if lst[i] == num:
            return True
        
        i += 1
    
    return False
        
def main():
    
    lista = [1,1,0,0]
    numero = 0
    
    print(estaEnLista1(numero,lista))
    print(estaEnLista2(numero,lista))
    print(estaEnLista3(numero,lista))
    
    return

main()