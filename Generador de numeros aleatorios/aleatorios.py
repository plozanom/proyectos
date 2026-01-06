# Versión en función de 'numeros_aleatorios.py'. Se introduce el limite inferior, superior y la cantidad de numeros aleatorios que se quieren
# Retorna una lista con todos los numeros aleatorios creados

from random import randint

def aleatorio(lim_i, lim_s, cantidad):
    num_aleatorios = []

    for i in range(cantidad):
        num_aleatorios.append(randint(lim_i, lim_s))
    
    return num_aleatorios