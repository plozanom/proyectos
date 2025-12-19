import os

def buscar_archivos(ruta_inicial):#, nombre_archivo):

    with os.scandir(ruta_inicial) as dirs:
        for dir in dirs:
            print(f"Ruta: {dir.path}")