def verificar(d,m,a):

    if(m == 2 and d == 29):
        if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            return True
        else:
            return False
    
    if   0 < d <= 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return True
    elif 0 < d <= 30 and (m == 4 or m == 6 or m == 9 or m == 11):
        return True
    else:
        return False

def main():
    
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if verificar(dia, mes, año):
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")

    return

main()