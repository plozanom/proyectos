bisiesto= int(input("Ingresa un año para verificar si es bisiesto: "))

if bisiesto %4 == 0 and bisiesto % 400 == 0 and bisiesto % 100 != 0:
    print(f"El año {bisiesto} es bisiesto")
else:
    print(f"El año {bisiesto} no es bisiesto")