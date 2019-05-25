def datosPersona(datos):
    
    print()
    print("Nombre: {}".format(datos[0]))
    print("Apellido: {}".format(datos[1]))
    print("Documento: {}".format(datos[2]))
    print()
    
    return

def extraerInfo():
    
    registro = open('persona.csv', 'r')
    datos = registro.readlines()
    registro.close()
    
    for i in range(len(datos)):
        if datos[i][-1]=='\n':
            datos[i]=datos[i][:-1]
    
    for i in range(len(datos)):
        datos[i]=datos[i].split(',')
    
    print(datos)

    return datos    

def aMinuscula(palabra):
    
    i=0
    palabra2=list(palabra)
    
    while i<len(palabra2):
        
        if 'A'<=palabra[i]<='Z':
            palabra2[i]=chr(ord(palabra2[i])+32)
        i+=1

    palabra = ''
    
    i=0
    
    while i<len(palabra2):
        palabra=palabra+palabra2[i]
        i+=1
    
    return palabra

def existeDni(dni):
    
    datos = extraerInfo()
    
    for i in range(len(datos)):
        if len(datos[i])==3:
            if dni == datos[i][2]: ##Posicion de los dni
                return True

    return False

def existeApellido(apellido):
    
    datos = extraerInfo()
    apellido = aMinuscula(apellido)
    
    for i in range(len(datos)):
        if len(datos[i])==3:
            if apellido == aMinuscula(datos[i][1]): ##Posicion de los dni
                return True

    return False


def agregarRegistro():
    
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese DNI:")
    
    while existeDni(dni):
        dni = input("DNI YA EXISTE. Corrobore los datos, por favor")
    
    registro = open('persona.csv', 'a')
    registro.write('{},{},{}\n'.format(nombre,apellido,dni))
    registro.close()


    return

def eliminarRegistro():

    datos = extraerInfo()
    dni = input('Ingrese el DNI: ')
    i = 0

    if datos[0][0] == '':
        del datos[0]

    while i < len(datos):
        if datos[i][2] == dni:
            del datos[i]

        i+=1

    registro = open('persona.csv', 'w')

    for i in datos:
        registro.write('{},{},{}\n'.format(i[0],i[1],i[2]))

    registro.close()
    
    
    
    
    return

def buscarRegistro():
    
    i=0
    print()
    parametro = input('Buscar por (dni/apellido): ')
    parametro = aMinuscula(parametro)
    
    while not parametro == 'dni' and not parametro == 'apellido':
        parametro = input('INGRESE CORRECTAMENTE EL DATO: ')
        parametro = aMinuscula(parametro)
    
    datos = extraerInfo()

    if parametro == 'dni':
        dni = input('Ingrese el DNI: ')
        
        if existeDni(dni):
            
            for dato in datos:
                if len(dato)==3:
                    if dato[2] == dni:
                        datosPersona(dato)
                        
        else:
            print("No existe el DNI")
        
    elif parametro == 'apellido':
        apellido = input('Ingrese el apellido: ')
        
        if existeApellido(apellido):
            for dato in datos:
                if len(dato)==3:
                    if aMinuscula(dato[1]) == aMinuscula(apellido):
                        datosPersona(dato)
        
        else:
            print("No existe el Apellido")
        
    
    return

def ordenarArchivo():
    
    i=0
    print()
    opcion = input('Ordenar por (1)-Nombre, (2)-Apellido, o (3)-DNI (Ingrese el numero): ')
    
    while not '1' <= opcion <= '3':
        opcion = input('INGRESE CORRECTAMENTE EL DATO: ')
    
    datos = extraerInfo()
    
    if opcion == '3':
        for i in range(len(datos)):
            for ix in range(len(datos)):
                if int(datos[i][2]) < int(datos[ix][2]):
                    memoria = datos[i]
                    datos[i] = datos[ix]
                    datos[ix] = memoria

    else:
        opcion = int(opcion)-1
        for i in range(len(datos)):
            for ix in range(len(datos)):
                if aMinuscula(datos[i][opcion]) < aMinuscula(datos[ix][opcion]):
                    memoria = datos[i]
                    datos[i] = datos[ix]
                    datos[ix] = memoria

    registro = open('persona.csv','w')##Se sobrescribe y se escribe los datos de manera ordenada
    
    for dato in datos:
        registro.write('{},{},{}\n'.format(dato[0],dato[1],dato[2]))

    registro.close()
   
    return


def mostrarArchivo():
    
    print()
    registro = registro = open('persona.csv','r')
    print(registro.read())
    registro.close()
    
    return



def mostrarMenu():
    
    print('1. AGREGAR REGISTRO')
    print('2. ELIMINAR REGISTRO')
    print('3. BUSCAR REGISTRO')
    print('4. ORDENAR ARCHIVO POR')
    print('5. MOSTRAR ARCHIVO')
    print('6. SALIR')

    return

def main():
    
    opcion = 0
    
    while not opcion == '6':
        
        mostrarMenu()
        opcion = input("Ingrese el valor de la opcion: ")
        
        if opcion == '1':
            agregarRegistro()
        elif opcion == '2':
            eliminarRegistro()
        elif opcion == '3':
            buscarRegistro()
        elif opcion == '4':
            ordenarArchivo()
        elif opcion == '5':
            mostrarArchivo()
        elif opcion == '6':
            print('Gracias por usar el programa! ')
        else:
            print('ERROR!')
            opcion = input("Ingrese el valor de la opcion: ")
    
    return

main()