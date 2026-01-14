# Función que crea de manera aleatoria una excusa que suene lo suficientemente creible.

from random import choice
import elementos

def excusa_aleatoria():
    return f"{choice(elementos.sujeto)} {choice(elementos.verbo)} {choice(elementos.adjetivo)} {choice(elementos.situacion)}"

print(excusa_aleatoria())