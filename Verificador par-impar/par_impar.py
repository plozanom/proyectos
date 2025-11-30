def verificador(num):

    if num % 2 == 0:
        return "par"
    
    return "impar"

numero = int(input("Ingrese un numero entero para verificar si es par o impar: "))

print(f"El numero {numero} es {verificador(numero)}")