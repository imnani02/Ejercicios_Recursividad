import random

cantidad = int(input("Ingrese la cantidad de elementos: "))

numeros = []

for i in range(cantidad):
    numero = random.randint(10, 99)
    numeros.append(numero)

suma = 0

for numero in numeros:
    if numero % 3 == 0:
        suma += numero

print("Lista generada:", numeros)
print("Suma de los multiplos de 3:", suma)