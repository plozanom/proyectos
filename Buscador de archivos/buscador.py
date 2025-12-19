import os

def buscar_archivos(ruta_inicial, nombre_archivo):

    with os.scandir(ruta_inicial) as dirs:
        for dir in dirs:
            if dir.is_file() and nombre_archivo.lower() in dir.name.lower():
                print(f"Ruta: {dir.path}")
