def multa(vv, vM, ve):
    
    if vM/2 <= vv <= vM:
        print("\nNo recibe multa")
        
    elif vM < vv < vM * 1.15: ##15% porciento menos/mas
        if ve:
            print("\nAdvertencia")
        else:
            print("\nNo recibe multa")
            
    elif vM * 0.95 < vv < vM:
        print("\nAdvertencia")
        
    elif vv > vM * 1.15:
        if ve:
            print("\nNo recibe multa")
        else:
            print("\nRecibe multa por exceso de velocidad")

    elif vv < vM * 0.95:
        if ve:
            print("\nNo recibe multa")
        else:
            print("\nRecibe multa por entorpecer el tránsito")



def main():
    
    velocidadVehiculo = float(input("Ingrese la velocidad: "))
    velocidadMaxima = float(input("Ingrese la velocidad máxima: "))
    vehiculoEmergencia = input("Emergencia (s/n): ")
    
    if vehiculoEmergencia.lower() == "s": ##.lower() hace todos los caracteres minuscula Esto se puede sacar pero para hacerlo mas entendible y se le da un valor del tipo booleano
        vehiculoEmergencia = True
    elif vehiculoEmergencia.lower() == "n":
        vehiculoEmergencia = False
    
    multa(velocidadVehiculo, velocidadMaxima, vehiculoEmergencia)
    
    return 0

main()