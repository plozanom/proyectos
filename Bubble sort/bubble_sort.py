# Ordenamiento burbuja o Bubble sort

def bubble_sort(vector):
    for paso in range(len(vector)-1):
        cambio = False
        for elemento in range(len(vector)-paso-1):
            if vector[elemento]>vector[elemento+1]:
                    temp = vector[elemento]
                    vector[elemento] = vector[elemento+1]
                    vector[elemento+1] = temp
                    cambio = True
        if cambio == False:
            break
    return vector