# Esta es una calculadora de potencias que solo funciona (de momento) con numeros enteros positivos en la parte del exponente
# Además es probable que proboque errores si se utilizan el cero y valores negativos
# Hay un montón de cosas que mejorar

def potencia(base = 1, exponente = 1):

    resultado = 1

    for i in range(exponente):
        resultado *= base

    return resultado