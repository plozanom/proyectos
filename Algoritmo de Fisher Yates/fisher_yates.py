from random import randint

def fisher_yates(lista):
    i = len(lista) - 1

    while i > 1:
        j = randint(0, i)
        lista[j], lista[i] = lista[i], lista[j]
        i -= 1
    
    return lista
