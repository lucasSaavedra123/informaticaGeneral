def promedio_parciales(p1,p2,p3):
    return ( p1 + p2 + p3 ) / 3

def promedio_general(p1,p2,p3,pc):
    return ( p1 + p2 + p3 + pc ) / 4


def main():
    parcial1 = float(input("Ingrese la nota del primer parcial: "))
    parcial2 = float(input("Ingrese la nota del segundo parcial: "))
    parcial3 = float(input("Ingrese la nota del tercer parcial: "))
    
    if (parcial1 >= 4 and parcial2 >= 4 and parcial3 >= 4) and ( promedio_parciales(parcial1, parcial2, parcial3) > 7 ):
        print("\nPromocionó la materia. Felicitaciones!")
        
    elif (parcial1 >= 4 and parcial2 >= 4 and parcial3 >= 4) and ( promedio_parciales(parcial1, parcial2, parcial3) <= 7 ):
        print("\nDeberá rendir exámen final.")
        
    elif parcial1 < 4 or parcial2 < 4 or parcial3 < 4:
        
        recuperatorio = float(input("Ingrese la nota del recuperatorio: "))
        
        if recuperatorio >= 4:
            print("\nPromedio general: {:.2f}".format(promedio_general(parcial1, parcial2, parcial3, recuperatorio)))
            print("Usted aprobó la materia. Felicitaciones!")
        else:
            print("\nFue aplazado de la materia.")


    return

main()