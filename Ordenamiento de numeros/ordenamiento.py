def obtencion_numeros(cantidad):

    lista_numeros = []

    for i in range(cantidad):
        numero = float(input(f"Ingrese un numero, escriba aqui el {i+1}o: "))
        lista_numeros.append(numero)

    return lista_numeros

def mayor_a_menor(cantidad):

    lista = obtencion_numeros(cantidad)
    lista = sorted(lista, reverse=True)

    return lista

def menor_a_mayor(cantidad):

    lista = obtencion_numeros(cantidad)
    lista = sorted(lista)

    return lista

def ordenamiento(lista):

    for i in lista:
        print(i)
