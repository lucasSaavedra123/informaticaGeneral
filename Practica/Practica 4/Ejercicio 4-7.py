def validacion(n):
    
    if not 1 <= n <= 10:
        return False
    else:
        return True

def ingresoDeNotas():
    
    cAplazos = 0
    cAprobados = 0
    cPromocionados = 0
    cAlumnos = 0
    sumaNotas = 0
    
    nota = int(input("Ingrese nota: "))
    
    while nota == 0:
        nota = int(input("ERROR! Ingrese al menos una nota: "))
    
    while not nota == 0:
        
        if validacion(nota):
            
            sumaNotas = nota + sumaNotas
            cAlumnos += 1 ##SUMA 1 a cAlumnos
            
            if nota < 4:
                cAplazos +=1
            elif 4 <= nota <= 7:
                cAprobados += 1
            elif nota > 7:
                cPromocionados +=1
        
        nota = int(input("Ingrese nota: "))
        
    print("\nCantidad de aplazos: {} ({:.2f}%)".format(cAplazos, porcentaje(cAplazos, cAlumnos)))
    print("Cantidad de aprobados: {} ({:.2f}%)".format(cAprobados, porcentaje(cAprobados, cAlumnos)))
    print("Cantidad de promocionados: {} ({:.2f}%)".format(cPromocionados, porcentaje(cPromocionados, cAlumnos)))

    print("Promedio general: {:.2f}".format(promedio(sumaNotas, cAlumnos)))

    return

def porcentaje(n,nTotal):
    return (n/nTotal) * 100

def promedio(nSuma, nCantidad):
    return nSuma / nCantidad



def main():
    
    ingresoDeNotas()
    
    return

main()