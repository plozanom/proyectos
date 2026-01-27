from random import choice
from time import sleep

import numpy as np


def tablero_vacio():
    tablero = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    return tablero


def espacios_vacios(tablero):
    coordenadas = [
        (i, j)
        for i in range(len(tablero))
        for j in range(len(tablero))
        if tablero[i][j] == 0
    ]

    return coordenadas


def jugada_automatica(tablero, jugador):
    coordenada_jugada = choice(espacios_vacios(tablero))
    tablero[coordenada_jugada] = jugador

    return tablero


def ganador(tablero, jugador):
    resultado = 0

    for jugador in [1, 2]:
        if (
            any((tablero == jugador).all(axis=1))
            or any((tablero == jugador).all(axis=0))
            or (np.diag(tablero) == jugador).all()
            or (np.diag(np.fliplr(tablero)) == jugador).all()
        ):
            resultado = jugador
    if (tablero != 0).all() and resultado == 0:
        resultado = -1

    return resultado


def tres_en_raya():
    tablero = tablero_vacio()
    resultado = 0
    print(f"{tablero}\n")
    sleep(1)

    while resultado == 0:
        for jugador in [1, 2]:
            tablero = jugada_automatica(tablero, jugador)
            print(f"{tablero}\n")
            sleep(1)
            resultado = ganador(tablero, jugador)

            if resultado != 0:
                break

    return resultado


def resultado():
    ganador = tres_en_raya()

    if ganador != -1:
        print(f"El ganador es el jugador {ganador}!")
    else:
        print("Se ha dado un empate")


resultado()
