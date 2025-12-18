# Función que recibe un año cualquiera y verifica si es bisiesto o no retornando True o False

def es_bisiesto(year): # Coloco year porque la ñ en año puede ser problematica y poner anno o anho no me parece bien
    if year %4 == 0 and year % 400 == 0 and year % 100 != 0:
        return True
    return False