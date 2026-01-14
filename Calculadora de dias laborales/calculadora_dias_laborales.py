# Función que calcula los días laborales entre dos fechas. Recibe como argumentos una fecha de inicio, una fecha final y una lista de días festivos (todos formateados con datetime.date)
# y devuelve el numero de días laborales entre dichas fechas.

from datetime import timedelta

def calculadora_dias_laborales(fecha_inicio, fecha_fin, festivos):
    fecha_actual = fecha_inicio
    dias_laborales = 0

    while fecha_actual <= fecha_fin:
        if fecha_actual.weekday() < 5 and fecha_actual not in festivos:
            dias_laborales += 1

        fecha_actual += timedelta(days= 1)

    return dias_laborales