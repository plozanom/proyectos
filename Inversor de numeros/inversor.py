# Varias funciones que invierten el orden de un numero entero

def inversor(numero):
    numero = str(numero)

    numero =  numero[::-1]

    return int(numero) # También se debería poder hacer solo poniendo int(str(numero)[::-1])

def invertir_matematicamente(numero):

    num_invertido = 0

    while numero > 0:
        
        digito = numero % 10
        num_invertido = (num_invertido * 10) + digito
        numero = numero//10
    
    return num_invertido