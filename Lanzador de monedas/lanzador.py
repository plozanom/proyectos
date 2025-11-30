from random import choice

opciones = ("cara", "cruz")

num_lanzamientos = int(input('Ingrese el numero de lanzamientos de la moneda: '))

cara = 0
cruz = 0

for lanzamiento in range(num_lanzamientos):
    moneda = choice(opciones)

    if moneda == 'cara':
        cara += 1
    else:
        cruz += 1

print(f'\nLos resultados del lanzamiento de monedas son:\nSe lanzaron {num_lanzamientos} monedas\nNumero de caras: {cara}   Porcentaje: {(cara/num_lanzamientos)*100}%\nNumero de cruces: {cruz}   Porcentaje: {(cruz/num_lanzamientos)*100}%')