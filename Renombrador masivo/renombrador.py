# Función que renombra de manera masiva archivos
# Recibe la ruta absoluta del directorio, el prefijo del nombre y la extensión de los archivos a renombrar
# Utiliza la extensión para saber qué archivos va a renombrar, evitando así otros archivos dentro de la carpetaç
# Cuando se coloque la extensión del archivo, no coloque el punto, ya está previsto

import os

def renombrador(dir_busqueda, prefijo, extension):

    with os.scandir(dir_busqueda) as dirs:
        contador = 0
        for dir in dirs:
            _, ext = os.path.splitext(dir)
            if dir.is_file() and ext == f'.{extension}':
                nuevo_nombre = f"{prefijo} {contador+1}{ext}"
                contador += 1
                os.rename(os.path.join(dir_busqueda, dir), os.path.join(dir_busqueda, nuevo_nombre))
    
    return "Cambio Hecho"