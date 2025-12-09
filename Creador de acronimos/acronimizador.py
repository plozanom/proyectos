# Una función llamada acronimizador (no se si siquiera es una palabra) que recibe una cadena y retorna un acronimo
# Si el texto tiene menos de 4 palabras, también incluirá en el nombre las preposiciones que contenga como "la" o "de"
 
def acronimizador(cadena):

    lista_caracteres = cadena.split(" ")
    caracateres_acronimo = []

    if len(lista_caracteres) > 3:
        for char in lista_caracteres:
            if len(char) > 3:
                caracateres_acronimo.append(char)
    else:
        caracateres_acronimo = lista_caracteres

    acronimo = ""
    
    for char in caracateres_acronimo:
        acronimo += char[0]

    return acronimo.upper()