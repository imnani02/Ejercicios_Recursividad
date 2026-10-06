inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))

if inicio < fin:
    maximo = 0

    for numero in range(inicio, fin + 1):
        if numero % 3 == 0:
            maximo = numero

    print("El máximo múltiplo de 3 es:", maximo)

else:
    minimo = 0

    for numero in range(inicio, fin - 1, -1):
        if numero % 3 == 0:
            minimo = numero

    print("El mínimo múltiplo de 3 es:", minimo)