# Cuenta las vocales en una cadena 

def contar_vocales(cadena):
    
    vocales = 0
    
    for letra in cadena:
        if letra.lower() in ('aeiou'):
            vocales += 1
    
    return vocales