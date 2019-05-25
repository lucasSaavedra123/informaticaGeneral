def extraerInfo(archivo):
    
    registro = open(archivo, 'r')
    datos = registro.readlines()
    registro.close()
    
    for i in range(len(datos)):
        if datos[i][-1]=='\n':
            datos[i]=datos[i][:-1]
    
    for i in range(len(datos)):
        datos[i]=datos[i].split(',')

    return datos  


def poblacion(ID_provincia):
    
    provincia = ''
    poblacion = 0
    
    datos = extraerInfo('provincias.txt')
    
    for dato in datos:
        if str(ID_provincia) == dato[0]:
            provincia = dato[1]
            
    datos = extraerInfo('localidades.txt')
    
    for dato in datos:
        if str(ID_provincia) == dato[2]:
            poblacion = int(dato[4])+poblacion
    
    print('{}: {} Habitantes'.format(provincia,poblacion))
    
    
    return

def localidadMaxima():
    
    poblacionMax = 0
    localidad = ''
    provincia = ''
    pais = ''
    ID_provincia = ''
    ID_pais = ''
    
    datos = extraerInfo('localidades.txt')

    for dato in datos:
        
        if poblacionMax < int(dato[4]):
            poblacionMax = int(dato[4])
            ID_provincia = dato[2]
            localidad = dato[1]
    
    datos = extraerInfo('provincias.txt')
    
    for dato in datos:
        if ID_provincia == dato[0]:
            provincia = dato[1]
            ID_pais = dato[2]
    
    datos = extraerInfo('paises.txt')
    
    for dato in datos:
        if ID_pais == dato[0]:
            pais = dato[1]
    
    
    print('Población: {}'.format(poblacionMax))
    print('Localidad: {}'.format(localidad))
    print('Provincia: {}'.format(provincia))
    print('País: {}'.format(pais))
    
    return





def main():
    
    poblacion(1)
    print()
    localidadMaxima()
    
    return

main()