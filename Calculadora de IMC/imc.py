peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso/(altura**2)

print(f"Su indice de masa corporal (IMC) es de {imc}")

if imc < 18.5:
    print("Se encuentra bajo de peso")
elif 18.5 <= imc < 25.0:
    print("Se encuentra dentro del peso normal")
elif 25.0 <= imc < 30.0:
    print("Tiene sobrepeso")
elif 30.0 <= imc < 35.0:
    print("Tiene obesidad grado I")
elif 35.0 <= imc < 40.0:
    print("Tiene obesidad grado II")
elif imc >= 40.0:
    print("Tiene obesidad grado III")