def ordenarAluXDNI(lst):
    
    memoria = 0
    
    for i in range(len(lst)):
        for ix in range(len(lst)):
            
            if lst[i][0] < lst[ix][0]:
                memoria = lst[i]
                lst[i]  = lst[ix]
                lst[ix] = memoria
    
    return

def cargarLstAlu(lstAlu):
    
    cargarAlu(lstAlu,2698705,'Lucas',18)
    cargarAlu(lstAlu,38698705,'Roberto',22)
    cargarAlu(lstAlu,35698705,'Lopez',15)
    
    return

def cargarAlu(lst,dni,nombre,edad):
    return lst.append([dni,nombre,edad])

def main():
    
    listaAlu = []
    cargarLstAlu(listaAlu)
    print(listaAlu)
    
    ordenarAluXDNI(listaAlu)
    
    print(listaAlu)
    return

main()