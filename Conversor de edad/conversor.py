print("Este 'programa' convierte la de edad de años a decadas, lustros, meses, días, horas, minutos y segundos")

edad = int(input("Por favor ingresa tu edad: "))

print(f"Tu edad en decadas es: {edad/10} decadas")
print(f"Tu edad en lustros es: {edad/5} lustros")
print(f"Tu edad en meses es: {edad*12} meses")
print(f"Tu edad en días es: {edad*365} días")
print(f"Tu edad en horas es: {edad*365*24} horas")
print(f"Tu edad en minutos es: {edad*365*24*60} minutos")
print(f"Tu edad en segundos es: {edad*365*24*60*60} segundos")