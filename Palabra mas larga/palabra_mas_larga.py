# Función que recibe una lista de palabras y retorna la palabra con mayor longitud

def palabra_mas_larga(lista_palabras):

    palabra_mayor = ''

    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mayor):
            palabra_mayor = palabra
    
    return palabra_mayor