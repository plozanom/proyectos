# Como el nombre lo indica, debe contar cuantos digitos hay en un numero entero
# Se que esto debería hacer una sola cosa, pero voy a agregarle que sume los digitos

def contar_digitos(numero):
    return len(str(numero))

def sumar_digitos(numero):

    suma = 0

    for digito in str(numero):
        suma += int(digito)
    
    return suma