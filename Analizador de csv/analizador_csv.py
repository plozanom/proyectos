# Función que recibe un archivo csv, analiza el archivo y muestra un numero de filas del documento
# Se debe instalar la librería pandas

import pandas as pd

def analizador_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)

        print(df[:10])
    except FileNotFoundError:
        print(f"El archivo {csv_file} no existe")