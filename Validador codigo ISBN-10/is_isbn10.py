# Función que recibe un codigo y si este es ISBN-10 retorna True, de lo contrario retorna False

def is_isbn10(code):
    
    vals = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'X':10}    
    counter = 0
    n = 10

    if code[-1] not in vals:
        return False

    for i in code:
        if i in vals:
            counter += vals[i] * n
            n -= 1

    return counter % 11 == 0
