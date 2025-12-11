# Función que recibe una lista de numeros y retorna el numero maximo y el minimo

def max_min(lista):

    lista = sorted(lista)
    return f"maximo: {lista[-1]}\nminimo: {lista[0]}"