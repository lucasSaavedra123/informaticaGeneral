def msjPositivo(n1,n2):
    print("\nEs posible cubrir el tendido.")
    print("Sugerencia:")
    print("{} unidades de caños de 1 metro".format(n1))
    print("{} unidades de caños de 5 metros".format(n2))
    return

def msjNegativo():
    return print("\nNo es posible cubrir el tendido")

def mensaje(c1,c5,cc):
##SE PRUEBAN LAS POSIBILIDADES

    u1 = 0
    u5 = 0
            
    while not (cc == 0 or c5 == 0 or cc < 5):
        u5 += 1
        c5 -= 1
        cc -= 5
                
    while not (cc == 0 or c1 == 0 or cc < 1):
        u1 += 1
        c1 -= 1
        cc -= 1
            
    if cc == 0:
        msjPositivo(u1,u5)
    else:
        msjNegativo()
        
    
    return
    
def main():
    
    cantidad1Metro  = int(input("Cantidad de caños de 1 metro: "))
    cantidad5Metros = int(input("Cantidad de caños de 5 metros:"))
    cantidadCubrir  = int(input("Metros totales a cubrir: "))
    
    mensaje(cantidad1Metro,cantidad5Metros, cantidadCubrir)
    
    return

main()