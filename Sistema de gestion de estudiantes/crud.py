# Funciones para la gestión de estudiantes en una clase cualquiera
# Se hace un CRUD básico sobre un arcivo CSV


import csv
from os import path


def archivo():
    base_de_datos = "Estudiantes.csv"
    if not path.exists(base_de_datos):
        with open(base_de_datos, "w") as db:
            csv.DictWriter(
                db,
                [
                    "ID",
                    "Nombre del Estudiante",
                    "1er cohorte",
                    "2do cohorte",
                    "3er cohorte",
                    "Nota Final",
                ],
            ).writeheader()


def crear_alumno(id, nombre, nota1="", nota2="", nota3=""):
    with open("Estudiantes.csv", "a") as db:
        escritor = csv.writer(db)
        escritor.writerow(
            [
                id,
                nombre,
                nota1,
                nota2,
                nota3,
                float(nota1) * 0.3 + float(nota2) * 0.3 + float(nota3) * 0.4,
            ]
        )


def leer_alumnos():
    with open("Estudiantes.csv", "r") as db:
        lector = csv.reader(db, delimiter=",")
        for fila in lector:
            for elemento in fila:
                print(elemento, end=" ")
            print(" ")


def leer_alumno(id):
    with open("Estudiantes.csv", "r") as db:
        lector = csv.reader(db, delimiter=",")
        for fila in lector:
            if fila[0] == str(id):
                for elemento in fila:
                    print(elemento, end=" ")


def actualizar_nota_alumno(id, numero_nota, valor_nota):
    actualizacion = []

    with open("Estudiantes.csv", "r") as db:
        lector = csv.reader(db, delimiter=",")
        actualizacion = list(lector)

    for fila in actualizacion:
        if fila[0] == str(id):
            fila[numero_nota + 1] = str(valor_nota)

    with open("Estudiantes.csv", "w") as db:
        escritor = csv.writer(db)
        escritor.writerows(actualizacion)


def actualizar_nombre_alumno(id, nuevo_nombre):
    actualizacion = []

    with open("Estudiantes.csv", "r") as db:
        lector = csv.reader(db, delimiter=",")
        actualizacion = list(lector)

    for fila in actualizacion:
        if fila[0] == str(id):
            fila[1] = nuevo_nombre

    with open("Estudiantes.csv", "w") as db:
        escritor = csv.writer(db)
        escritor.writerows(actualizacion)


def borrar_alumno(id):
    actualizacion = []

    with open("Estudiantes.csv", "r") as db:
        lector = csv.reader(db, delimiter=",")
        actualizacion = list(lector)

    # for fila in actualizacion:
    #     if fila[0] == str(id):
    #         actualizacion.pop()
    actualizacion.pop(id - 1)

    with open("Estudiantes.csv", "w") as db:
        escritor = csv.writer(db)
        escritor.writerows(actualizacion)


# archivo()
# crear_alumno(1, "Laura Gómez", "4.5", "3.8", "4.2")
# crear_alumno(2, "Carlos Pérez", "3.6", "3.9", "4.0")
# crear_alumno(3, "Valentina Rodriguez", "4.7", "4.3", "4.8")
# leer_alumnos()
# print()
# leer_alumno(3)
# actualizar_nota_alumno(1, 2, 3.8)
# leer_alumnos()
# crear_alumno(4, "Andrés Torres", "2.9", "3.1", "3.5")
# print()
# leer_alumno(4)
# print()
# actualizar_nombre_alumno(4, "Andrés Flores")
# leer_alumno(4)
# borrar_alumno(1)
# leer_alumnos()
