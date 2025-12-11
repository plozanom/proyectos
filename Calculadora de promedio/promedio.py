# Función que recibe una lista de numeros y retorna el promedio de dichos numeros

def promedio(lista):

    sumatoria = 0

    for num in lista:
        sumatoria += num

    return sumatoria/len(lista)