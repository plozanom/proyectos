# Función que lanza un numero n de monedas al azar y retorna en un diccionario el numero de caras y cruces conseguidos

from random import choice

def lanzador_monedas(lanzamientos):

    opciones = ("cara", "cruz")
    cara = 0
    cruz = 0

    for lanzamiento in range(lanzamientos):
        moneda = choice(opciones)

        if moneda == 'cara':
            cara += 1
        else:
            cruz += 1

    return {"cara": cara, "cruz": cruz}