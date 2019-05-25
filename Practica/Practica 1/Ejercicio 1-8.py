segundos = int(input("Ingrese tiempo en segundos: "))

dias = int(segundos / 86400)
horas = int(( segundos / 3600 ) - ( 24 * dias ))
minutos = int(segundos / 60 - (60 * horas + dias * 24 * 60))
segundos = int(segundos - (3600 * horas + 60 * minutos + dias * 86400))

print(int(dias), " dias(s)", int(horas), " hora(s)", int(minutos), " minuto(s)", int(segundos), " segundo(s).")