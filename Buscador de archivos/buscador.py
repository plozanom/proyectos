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