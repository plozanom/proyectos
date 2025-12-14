def minusculas(cadena):
    return cadena.lower()

def filtrado(cadena):

    lista = []

    for letra in cadena:
        if letra.isalpha():
            lista.append(letra)
    
    return lista

def es_anagrama(cadena1, cadena2):


    cadena1 = minusculas(cadena1)
    cadena2 = minusculas(cadena2)

    lista1 = filtrado(cadena1)
    lista2 = filtrado(cadena2)

    return sorted(lista1) == sorted(lista2)