# Función que recibe los nombres y apellidos de una persona y retorna un nombre de usuario

from random import randint

def generador_usuario(nombres, apellidos):

    lista_apellidos = apellidos.lower().split()

    return nombres[0].lower() + lista_apellidos[0] + str(randint(2, 1000))