# Función que recibe dos tuplas de coordenadas (x, y) y halla la distancia entre esos dos puntos

def distancia(coord1, coord2):
    return ((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2)**0.5