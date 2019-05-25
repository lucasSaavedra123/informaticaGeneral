"""Permitir que el usuario cree diccionarios"""
"""Va ser parecido al ejercicio 3 de la practica"""

def agregar(dic):
    
    pais = input("Ingrese el nombre del pais: ")
    ciudad = input("Ingrese su ciudad capital: ")
    
    dic[pais]=ciudad ##Se van creando
    
    return

def borrar(dic):
    borrar = input("Ingrese el pais/ciudad a eliminar: ")
    
    if borrar in capitales.keys():
        del capitales[pais]
    else:
        if borrar not in dic.values():
            print("No se encontro dicho pais o ciudad.")
        else:
            for indice in dic.copy():##Si no se pone copy falla pq modificamos la lista en el ciclo Se toma una copia de la lista original
                if dic[indice] == borrar:
                    del dic[indice]
        
    return

def buscar(dic):
    print(dic.get(input("Ingrese el pais: ")))##Si no esta 
    return

def vaciar(dic):
    ##dic.clear() ##No se puede usar pero vacia el diccionario
    ##Ni tampoco dic = {} ya que perdemos conexion con del dic del main
    for indice in dic.copy():
        del dic[indice]
    
    
    return

def mostrar(dic):
    for pais in dic: ##Toma los indices
        print(pais, "->", dic[pais])
    
    return


def opcionMenu():
    print("1-Agregar")
    print("2-Borrar")
    print("3-Buscar")
    print("4-Vaciar")
    print("5-Mostrar")
    print("6-Salir")
    o = int(input("Ingrese su opcion: "))
    
    while not (0 <= o <= 6):
        o=int(input("Error.Ingrese otra vez: "))
        
    return o
    
def main():
    
    capitales = dict()##Condicion que crea diccionario
    capitales = {'Argentina':'Buenos Aires', 'Uruguay': 'Montevideo'}
    
    opc = opcionMenu()

    while opc != 6:
        if opc == 1:
            agregar(capitales)
        elif opc == 2:
            borrar(capitales)
        elif opc == 3:
            buscar(capitales)
        elif opc == 4:
            vaciar(capitales)
        elif opc == 5:
            mostrar(capitales)
        
        opc = opcionMenu()
        
    return

main()