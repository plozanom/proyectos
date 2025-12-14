# Una función que recibe una lista de numeros y retorna un diccionario ordenado cuya clave es el numero y el valor es la frecuencia en que se encuentra repetido
# Luego, otra función, utilizando un bucle for muestra un histograma simple de frecuencias

def frecuencia_numeros(lista):

    diccionario = {}
    
    for numero in lista:
        if numero in diccionario:
            diccionario[numero] += "|"
        else:
            diccionario[numero] = "|"

    diccionario = dict(sorted(diccionario.items(), key= lambda item: item[0]))

    return diccionario

def histograma(lista):
    diccionario = frecuencia_numeros(lista)

    for clave, valor in diccionario.items():
        print(f"{clave}: {valor} {len(valor)}")

numeros = [
    44, 67, 52, 52, 61, 48, 70, 55, 55, 55,
    63, 41, 49, 49, 60, 60, 60, 46, 58, 58,
    58, 58, 42, 69, 53, 53, 47, 47, 47, 64,
    64, 64, 64, 64, 51, 51, 51, 40, 68, 68,
    45, 45, 45, 45, 45, 57, 57, 62, 62, 62,
    66, 66, 50, 50, 50, 50, 50, 50, 43, 43,
    43, 59, 59, 59, 54, 54, 65, 65, 65, 65,
    65, 65, 65, 56, 56, 56, 56, 56, 71-1,
    70, 70, 70, 48, 48, 48, 61, 61, 61,
    41, 41, 67, 67, 67, 52, 52, 52
]

histograma(numeros)