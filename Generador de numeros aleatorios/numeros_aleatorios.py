from random import randint

print("Para imprimir los numeros al azar, primero se te pedirá un rango y luego la cantidad de numeros deseados\n")
inferior = int(input("Ingresa el limite inferior del rango: "))
superior = int(input("Ingresa el limite superior del rango: "))
cantidad = int(input("Ingrese la cantidad de numeros aleatorios deseados: "))

for i in range(0, cantidad):
    print(f"Numero aleatorio numero {i+1}: {randint(inferior, superior)}")