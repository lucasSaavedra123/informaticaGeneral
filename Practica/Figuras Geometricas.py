"""
Se usan las variables F (filas) y C (columnas)
y se usa el 'for' y en el caso de querer omitir 'coordenadas' (querer imprimir * o un espacio)
se usa un 'if' para poder elegir que se imprima * o un espacio

En el caso de que haya diagonales hay que ver estas primero
y se ve la similitud que hay.

Con OR se hace la suma de figuras
y con AND se logra la interseccion de las figuras
Si se quiere sacar una parte de la figura podemos usar el AND NOT y se saca esa parte.

"""
n = 5

for f in range(n):
    
    for c in range (n):
        
        if (f-c >= 0 and f+c <= n - 1) or (f-c <= 0 and f+c >= n - 1):
            print("*", end = "")
        else:
            print(" ", end = "")
    
    print()