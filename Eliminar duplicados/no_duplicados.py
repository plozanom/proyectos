# Función que recibe una lista de numeros y retorna una nueva lista sin duplicados de numeros

def no_duplicados(lista):
    no_repetidos = list(dict.fromkeys(lista))

    return no_repetidos