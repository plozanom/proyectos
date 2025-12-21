# Función que halla la edad exacta
# Recibe año, mes y día de nacimiento y retorna cuantos años, meses y días han pasado

import datetime

def edad_exacta(year, month, day):

    nacimiento = datetime.datetime(year, month, day)
    hoy = datetime.datetime.today()

    años = hoy.year - nacimiento.year
    meses = hoy.month - nacimiento.month
    dias = hoy.day - nacimiento.day

    if dias < 0:
        dias += (hoy.replace(day=1) - datetime.timedelta(days=1)).day # Truco sacado de Gemini, ya me había cansado de pensar en una solución
        meses -= 1

    if meses < 0: # Se puede dar el caso que al hallar los meses de negativo (Ej.: marzo(3) - junio(6) = -3)
        meses += 12
        años -= 1
    
    return f"Edad: {años} años {meses} meses {dias} dias"