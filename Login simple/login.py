# La función registrar permite el ingreso de un nuevo usuario y contraseña, crea la 'base de datos' si no existe y retorna que el registro ha sido hecho
# La función login revisa si el usuario y la contraseña se encuentran en el archivo, si los datos son correctos, mostrará una bienvenida de lo contrario
# mostrará un aviso acerca de un error en los datos suministrados
# Nota: Los datos pasados a la función login deben ser de tipo string

import csv
from os import path

def registrar(usuario, password):

    archivo = "base de datos.csv"

    if not path.exists(archivo):
        with open(archivo, "w", encoding= "utf-8") as bd:
            csv.DictWriter(bd, ["usuario", "contraseña"]).writeheader()

    with open(archivo, "a") as bd:
        writer = csv.writer(bd)
        writer.writerow([usuario, password])

    return "Registro hecho con exito"

def login(usuario, password):

    with open("base de datos.csv", "r") as bd:
        reader = csv.DictReader(bd)
        for row in reader:
            if row["usuario"] == usuario and row["contraseña"] == password:
                return f"Bienvenido {usuario}"
            
    return "Usuario y/o contraseña no validos"

print(login("test", "3456"))