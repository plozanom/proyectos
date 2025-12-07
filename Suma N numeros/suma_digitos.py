# Esta función debe sumar los numeros de uno en uno desde el 1 hasta el numero que se introduzca (N).

def suma_n(n):

    suma = 0

    for i in range(n+1):
        suma += i

    return suma