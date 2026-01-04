# Funciones creadas para la suma de dos matrices n*n
# La primera función separa la creación de las matrices de la suma de las matrices,
# recibe el tamaño de la fila (n) y una lista de valores dados por el usuario y retorna una matriz n*n
# La segunda función llama a la primera función y hace la suma de dos matrices cuadradas,
# por lo que se deben introducir tanto el tamaño de la fila como las listas de valores para cada matriz


def crear_matriz(n, valores):
    return [valores[i * n : (i + 1) * n] for i in range(n)]


def suma_matrices(n, valores_m1, valores_m2):
    matriz1 = crear_matriz(n, valores_m1)
    matriz2 = crear_matriz(n, valores_m2)
    return [[matriz1[i][j] + matriz2[i][j] for j in range(n)] for i in range(n)]
