def extraerHabitantes():
    
    lstHabitantes = []
    archivo = open('habitantes.txt','r')
    
    for habitante in archivo.readlines():
        
        if habitante[-1] == '\n':
            habitante = habitante[:-1]
        
        if not habitante == '':
            habitante = habitante.split(',')
            habitante[0]=int(habitante[0])
            habitante[2]=int(habitante[2])
            habitante[3]=int(habitante[3])
            
            lstHabitantes.append(habitante)
    
    archivo.close()
    
    return lstHabitantes

def extraerLocalidades():
    
    lstLocalidades = []
    archivo = open('localidades.txt','r')
    
    for localidad in archivo.readlines():
        
        if localidad[-1] == '\n':
            localidad = localidad[:-1]
        
        if not localidad == '':
            localidad = localidad.split(',')
            localidad[0]=int(localidad[0])
            localidad[2]=int(localidad[2])
            
            lstLocalidades.append(localidad)
    
    archivo.close()
    
    return lstLocalidades


def extraerHabXLoc():
    
    lstHabXLoc = []
    archivo = open('habitantesXlocalidad.txt','r')
    
    for info in archivo.readlines():
        
        if info[-1]=='\n':
            info = info[:-1]
        
        if not info == '':
            info = info.split(',')
            info[0]=int(info[0])
            info[1]=int(info[1])
            
            lstHabXLoc.append(info)
    
    archivo.close()
    
    return lstHabXLoc


def cantHabitantes(nombreLocalidad, hijos):
    
    ID_localidad = 0
    lista=[]
    
    lstLocalidades = extraerLocalidades()
    lstHabitantes =  extraerHabitantes()
    lstHabXLoc = extraerHabXLoc()
    
    for localidad in lstLocalidades:
        if nombreLocalidad == localidad[1]:
            ID_localidad = localidad[0]
            
    for habitante in lstHabitantes:
        for habXLoc in lstHabXLoc:
            if ID_localidad == habXLoc[0] and habXLoc[1] == habitante[0] and habitante[2]==hijos:
                lista.append([habitante[0],habitante[1]])

    return lista

def edadXlocalidad():
    
    lstHabXLoc = extraerHabXLoc()
    lstHabitantes = extraerHabitantes()
    memoria = 0
    lst = []
    edades = []
    lstImprimir = []
    
    for habXLoc in lstHabXLoc:
        for habitante in lstHabitantes:
            if habitante[0] == habXLoc[1]:
                lst.append([habXLoc[0],habitante[3]])
        
    ordenarLista(lst,0)
    
    
    for dato in lst:
        
        if lstImprimir == [] and edades == []:
            memoria = dato[0]
            edades.append(dato[1])
            
        else:
            if memoria == dato[0]:
                edades.append(dato[1])
            else:
                lstImprimir.append([memoria,edades])
                memoria = dato[0]
                edades = []
                edades.append(dato[1])
    
    lstImprimir.append([memoria,edades])
    
    for i in range(len(lstImprimir)):
       lstImprimir[i][1]=prom(lstImprimir[i][1])
    
    
    ##Se imprime:
    
    print('{:<15}{:<15}'.format('Id localidad','Promedio Edad'))
    
    for i in lstImprimir:
        print('{:<15}{:<15}'.format(i[0],i[1]))
    
    
    return

def prom(lst):
    
    i = 0
    prom = 0
    sum = 0
    
    for i in range(len(lst)):
        sum = sum + lst[i]
    
    return sum / (i + 1)



def ordenarLista(lst,campo):
    
    for j in range(len(lst)):
        for l in range(len(lst)):
            if lst[j][campo] < lst[l][campo]:
                lst[j],lst[l]=lst[l],lst[j]
    return


def main():
    print(cantHabitantes('Adolfo Alsina', 1))
    edadXlocalidad()
    return

main()
    