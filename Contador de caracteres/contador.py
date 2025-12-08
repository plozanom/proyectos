# 1. Una función llamada frecuencia_caracteres que recibe una cadena de texto y retorna un diccionario con la frecuencia de cada caracter
# 2. Una función llamada contar_palabras que cuenta el numero de palabras en una cadena de texto

def frecuencia_caracteres(cadena):
    lista = list(cadena)
    lista = sorted(lista)

    diccionario = {}
    
    for letra in lista:
        if letra.lower() in diccionario:
            diccionario[letra.lower()] += 1
        else:
            diccionario[letra.lower()] = 1

    return diccionario

def contar_palabras(cadena):
    lista_palabras = cadena.split(" ")
    
    return len(lista_palabras)