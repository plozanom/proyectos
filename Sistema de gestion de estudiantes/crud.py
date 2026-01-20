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
            if fila[0] == id:
                for elemento in fila:
                    print(elemento, end=" ")


def actualizar_alumno():
    pass


def borrar_alumno():
    pass


# archivo()
# crear_alumno(1, "Laura Gómez", "4.5", "3.8", "4.2")
# crear_alumno(2, "Carlos Pérez", "3.6", "3.9", "4.0")
# crear_alumno(3, "Valentina Rodriguez", "4.7", "4.3", "4.8")
# leer_alumnos()
# print()
# leer_alumno("3")
