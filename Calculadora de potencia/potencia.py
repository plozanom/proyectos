#Esta es una calculadora de potencias que solo funciona (de momento) con numeros enteros en la parte del exponente

def potencia(base = 1, exponente = 0):

    resultado = 1

    for i in range(exponente):
        resultado *= base

    return resultado


prueba = potencia(2, 3)

print(prueba)