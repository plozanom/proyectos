# Debe validar si la contraseña es mayor a 8 caracteres
# Debe validar si hay por lo menos una mayuscula
# Debe validar si hay por lo menos una minuscula
# Debe validar si hay caracteres especiales

import string

def validador(pswd):
    
    lista_bool = []

    if len(pswd) < 8:
        return "La contraseña no es valida"
    else:
        mayus = any(char.isupper() for char in pswd)
        lista_bool.append(mayus)

        minus = any(char.islower() for char in pswd)
        lista_bool.append(minus)
        
        digit = any(char.isdigit() for char in pswd)
        lista_bool.append(digit)

        espec = any(char in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for char in pswd)
        lista_bool.append(espec)

    for j in lista_bool:
        if j == False:
            return "La contraseña no es valida"
    return "La contraseña es valida"