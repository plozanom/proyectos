# Una de las funciones es para hallar los divisores de un numero
# La otra función es para hallar si un numero es divisible por otro
# Obviamente los numeros a evaluar deben ser enteros

def divisores(numero):

    print(f"Los divisores de {numero} son: ")

    for i in range(2, numero):
        if numero % i == 0:
            print(i, end=' ')
    
    print("")

def es_divisible(num1, num2):

    if num1 % num2 == 0:
        return f"{num1} es divisible entre {num2}"
    
    return f"{num1} no es divisible entre {num2}"