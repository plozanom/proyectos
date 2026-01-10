import random

# 1. Definimos dimensiones (siempre impares para tener bordes)
filas = 21
columnas = 21

# 2. Creamos la matriz llena de paredes (1)
laberinto = [[1 for _ in range(columnas)] for _ in range(filas)]

# 3. Punto de inicio y preparación
inicio = (1, 1)
laberinto[inicio[0]][inicio[1]] = 0 # Marcamos el inicio como camino
pila = [inicio]

while pila:
    f, c = pila[-1] # Miramos la posición actual (sin sacarla aún)
    vecinos = []

    # Posibles movimientos de 2 en 2
    posibles = [
        (f - 2, c, f - 1, c), # Arriba (destino_f, destino_c, medio_f, medio_c)
        (f + 2, c, f + 1, c), # Abajo
        (f, c - 2, f, c - 1), # Izquierda
        (f, c + 2, f, c + 1)  # Derecha
    ]

    for nf, nc, mf, mc in posibles:
        # Aquí aplicaríamos tus condiciones: ¿está dentro y es pared?
        if 0 < nf < filas - 1 and 0 < nc < columnas - 1 and laberinto[nf][nc] == 1:
            vecinos.append((nf, nc, mf, mc))

    if vecinos:
        # Elegimos uno al azar y "picamos" el camino
        nf, nc, mf, mc = random.choice(vecinos)
        laberinto[mf][mc] = 0
        laberinto[nf][nc] = 0
        pila.append((nf, nc)) # Avanzamos a la nueva celda
    else:
        pila.pop() # No hay salida, retrocedemos (Backtracking)

def imprimir_laberinto(matriz):
    for fila in matriz:
        # Convertimos cada 1 en '#' y cada 0 en un espacio ' '
        linea = "".join(["#" if celda == 1 else " " for celda in fila])
        print(linea)

# Probamos imprimirlo después de generar
imprimir_laberinto(laberinto)