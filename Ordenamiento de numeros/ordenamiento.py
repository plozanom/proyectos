cantidad = int(input("Ingrese la cantidad de numeros que quiere ordenar: "))

def obtencion_numeros(cantidad):

    lista_numeros = []

    for i in range(cantidad):
        numero = float(input(f"Ingrese un numero, escriba aqui el {i+1}o: "))
        lista_numeros.append(numero)

    return lista_numeros

def mayor_a_menor(lista):

    lista = sorted(lista, reverse=True)

    return lista

def menor_a_mayor(lista):

    lista = sorted(lista)

    return lista

def ordenamiento(lista):

    for i in lista:
        print(i)

paso1 = obtencion_numeros(cantidad)
paso2 = mayor_a_menor(paso1)

print("\nDebajo se muestran los numeros ordenados")
ordenamiento(paso2)