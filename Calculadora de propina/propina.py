valor_consumido = int(input("Ingrese el valor del articulo consumido: "))
porcentaje_propina = int(input("Ingrese el porcentaje de propina: "))

propina = valor_consumido*(porcentaje_propina/100)
total = valor_consumido + propina

print(f"Su total a pagar es {total} incluyendo una propina del {porcentaje_propina}%")