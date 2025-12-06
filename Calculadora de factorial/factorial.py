# Calcula el factorial de un numero entero positivo (tener cuidado con numeros muy grandes)


def factorial(num):

    fact = 1

    for i in range(num):
        fact *= (i+1)
    
    return fact