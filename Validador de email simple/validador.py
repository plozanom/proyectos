# Función que recibe un email y comprueba si contiene '@' y '.', no valida nada más

def validar_email_simple(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False