# Cajero automatico basico, se puede revisar saldo, hacer retiros y hacer depositos.
# Funciones:
#   - crear_saldo(): Crea un archivo csv (si no existe) con las cabeceras 'Saldo', 'Tipo de Movimiento', 'Valor Cambio' y 'Marca de Tiempo' con un saldo inicial de $100000
#   - ultimo_saldo(): Busca y retorna el ultimo saldo registrado en el csv
#   - retiro(): Recibe un valor a retirar y esta función verifica si el saldo es suficiente, si es así, realiza el retiro y lo registra, de lo contrario, avisa del saldo insuficiente
#   - deposito(): Recibe un valor a depositar y retorna el deposito exitoso
#   - saldo(): Muestra en pantalla el ultimo saldo

import csv
from os import path
from datetime import datetime

def crear_saldo():

    archivo = "Saldo cajero.csv"

    if not path.exists(archivo):
        with open(archivo, "w") as bd:
            csv.DictWriter(bd, ["Saldo", "Tipo de Movimiento", "Valor Cambio", "Marca de Tiempo"]).writeheader()
            writer = csv.writer(bd)
            writer.writerow([100000, "-", 0, datetime.now().strftime("%Y-%m-%d-%H:%M:%S")])

def ultimo_saldo():
    with open("Saldo cajero.csv", "r") as bd:
        reader = list(csv.reader(bd))        
        return reader[-1][0]

def retiro(valor_retiro):

    saldo = ultimo_saldo()

    if valor_retiro > float(saldo):
        return "No hay saldo suficiente"
    else:
        with open("Saldo cajero.csv", "a") as bd:
            writer = csv.writer(bd)
            writer.writerow([float(saldo) - valor_retiro, "Retiro", f"-{valor_retiro}", datetime.now().strftime("%Y-%m-%d-%H:%M:%S")])
            return "Retiro exitoso"

def deposito(valor_deposito):
    
    saldo = ultimo_saldo()

    with open("Saldo cajero.csv", "a") as bd:
        writer = csv.writer(bd)
        writer.writerow([float(saldo) + valor_deposito, "Deposito", f"+{valor_deposito}", datetime.now().strftime("%Y-%m-%d-%H:%M:%S")])
        return "Deposito exitoso"

def saldo():
    return f"Su saldo es de ${ultimo_saldo()}"

print(saldo())