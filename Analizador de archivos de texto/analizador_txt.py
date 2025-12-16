# Función que analiza archivos txt recibiendo el nombre del archivo (si se encuentra en la misma carpeta) y devuelve un diccionario
# con el numero de lineas, el numero de palabras y el numero de caracteres

def analizador_txt(nombre_archivo):

    analisis = {}

    with open( nombre_archivo, 'r') as file:
        lineas = file.readlines()
        analisis['num lineas'] = len(lineas)

    with open( nombre_archivo, 'r') as file:
        contenido = file.read()
        palabras = contenido.split()
        analisis['num palabras'] = len(palabras)
        analisis['num caracteres'] = len(contenido)

    return analisis