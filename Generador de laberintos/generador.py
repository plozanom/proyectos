# Funciones para generar, resolver y visualizar el laberinto

import random
import time
import os

def generar_laberinto(filas, columnas):
    # Inicializamos con paredes
    lab = [[1 for _ in range(columnas)] for _ in range(filas)]
    pila = [(1, 1)]
    lab[1][1] = 0
    
    while pila:
        f, c = pila[-1]
        vecinos = []
        for nf, nc, mf, mc in [(f-2, c, f-1, c), (f+2, c, f+1, c), (f, c-2, f, c-1), (f, c+2, f, c+1)]:
            if 0 < nf < filas-1 and 0 < nc < columnas-1 and lab[nf][nc] == 1:
                vecinos.append((nf, nc, mf, mc))
        
        if vecinos:
            nf, nc, mf, mc = random.choice(vecinos)
            lab[mf][mc] = 0
            lab[nf][nc] = 0
            pila.append((nf, nc))
        else:
            pila.pop()
    return lab

def generar_laberinto_animado(filas, columnas, vel=0.02):
    lab = [[1 for _ in range(columnas)] for _ in range(filas)]
    pila = [(1, 1)]
    lab[1][1] = 0
    
    while pila:
        f, c = pila[-1]

        # Se limpia la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

        # Se dibuja de manera gradual la creación del laberinto
        for fila in lab:
            print("".join(["#" if celda == 1 else " " for celda in fila]))
        
        time.sleep(vel)

        vecinos = []
        for nf, nc, mf, mc in [(f-2, c, f-1, c), (f+2, c, f+1, c), (f, c-2, f, c-1), (f, c+2, f, c+1)]:
            if 0 < nf < filas-1 and 0 < nc < columnas-1 and lab[nf][nc] == 1:
                vecinos.append((nf, nc, mf, mc))
        
        if vecinos:
            nf, nc, mf, mc = random.choice(vecinos)
            lab[mf][mc] = 0
            lab[nf][nc] = 0
            pila.append((nf, nc))
        else:
            pila.pop()
    return lab

def resolver_laberinto(lab, inicio=(1, 1) , fin=None):

    # Si no se pasa el argumento para fin, se halla con la siguiente condición
    if fin is None:
        fin = (len(lab) - 2, len(lab[0]) - 2)

    cola = [inicio]
    visitados = {inicio}
    padres = {}
    
    while cola:
        # 1. Sacamos el primero
        actual = cola.pop(0)
        
        # 2. Si llegamos, dejamos de buscar
        if actual == fin:
            break
        
        # 3. Explorar vecinos
        f, c = actual
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vf, vc = f + df, c + dc
            vecino = (vf, vc)
            
            # Verificamos límites, si es camino y si no lo visitamos
            if 0 <= vf < len(lab) and 0 <= vc < len(lab[0]) and \
               lab[vf][vc] == 0 and vecino not in visitados:
                
                visitados.add(vecino)
                padres[vecino] = actual
                cola.append(vecino)
    actual = fin
    while actual != inicio:
        f, c = actual
        lab[f][c] = 2
        actual = padres[actual]
    lab[inicio[0]][inicio[1]] = 2

def imprimir(lab):
    for fila in lab:
        print("".join(["#" if c == 1 else "." if c == 2 else " " for c in fila]))

# Configuración inicial
F, C = 31, 31 
mi_laberinto = generar_laberinto_animado(F, C)
resolver_laberinto(mi_laberinto, (1, 1), (F-2, C-2))
imprimir(mi_laberinto)