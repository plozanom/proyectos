# Una función que recibe un texto y retorna True si es un palindromo o False de lo contrario

def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    cadena_invertida = cadena[::-1]

    if cadena == cadena_invertida:
        return True
    
    return False