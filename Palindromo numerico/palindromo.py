# Una función para hallar si un numero entero es un palindromo

def es_palindromo(numero):

    numero_invertido = int(str(numero)[::-1])

    if numero_invertido == numero:
        return f"{numero} es un palindromo"
    
    return f"{numero} no es un palindromo"