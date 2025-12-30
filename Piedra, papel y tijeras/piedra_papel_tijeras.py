# Nucleo del juego Piedra, papel o tijeras, donde el usuario debe escoger Piedra -> "r", Papel -> "p" o Tijeras -> "s" para competir contra la cpu
# retornando "Empate" si es un empate, "Ganaste" en caso de que el usuario gane y "Perdiste" si el ususario pierde

from random import choice

def piedra_papel_tijeras(usuario):

    opciones = ("r", "p", "s")
    ganar = [("r", "s"), ("s", "p"), ("p", "r")]
    computadora = choice(opciones)
    usuario = usuario.lower()

    if usuario == computadora:
        return "Empate"
    elif (usuario, computadora) in ganar:
        return "Ganaste"
    else:
        return "Perdiste"