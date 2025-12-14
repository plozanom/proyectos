# Función que recibe una matriz (una lista de listas) y retorna la matriz transpuesta

def transponer_matriz(matriz):
    
    # Si no hay matriz, retorna una matriz vacía
    if not matriz:
        return []

    # Obtener el número de filas y columnas de la matriz original
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Crear la matriz con filas y columnas invertidas (transpuesta) e inicializarla con ceros
    matriz_transpuesta = [[0 for _ in range(num_filas)] for _ in range(num_columnas)]

    # Llenar la matriz transpuesta
    for i in range(num_filas):         # Recorre las filas de la matriz original
        for j in range(num_columnas):  # Recorre las columnas de la matriz original
            matriz_transpuesta[j][i] = matriz[i][j]

    return matriz_transpuesta