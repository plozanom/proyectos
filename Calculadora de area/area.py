from math import pi

PI = pi

def area_circulo(rad):
    return PI*(rad**2)

def area_triangulo(base, altura):
    return (base*altura)/2

def area_cuadrado(lado):
    return lado**2

def area_rectangulo(base, altura):
    return base*altura

def area_trapecio(base1, base2, altura):
    return ((base1 + base2)*altura)/2 

def area_rombo(diag1, diag2):
    return (diag1*diag2)/2