# Función que recibe un titulo y retorna las palabras capitalizadas

def formateador(cadena):
    lista_palabras = cadena.split(" ")
    lista_capitalizada = []

    for palabra in lista_palabras:
        lista_capitalizada.append(palabra.capitalize())
    
    return " ".join(lista_capitalizada)
