# Función la cual recibe una ruta de directorio (ruta absoluta) y un nombre o fragmento de nombre de un archivo
# Busca de manera recursiva en las subcarpetas del directorio (no se ha probado la busqueda en subcarpetas de subcarpetas )
# Muestra en pantalla las rutas de los posibles archivos que concuerdan con la busqueda.

import os

def buscar_archivos(ruta_inicial, nombre_archivo):

    try:
        with os.scandir(ruta_inicial) as dirs:
            for dir in dirs:
                if dir.is_file() and nombre_archivo.lower() in dir.name.lower():
                    print(f"Ruta: {dir.path}")
                elif dir.is_dir(follow_symlinks=False):
                    buscar_archivos(dir.path, nombre_archivo)

    except FileNotFoundError:
        print(f"La ruta {ruta_inicial} no existe")
    except PermissionError:
        print(f"No tienes permiso para la ruta {ruta_inicial}")