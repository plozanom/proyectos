# Cifrado Cesar sencillo

def cesar(mensaje, desplazar):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    texto_encriptado = ''

    for char in mensaje.lower():
        if char == ' ':
            texto_encriptado += char
        else:
            indice = alfabeto.find(char)
            nuevo_indice = (indice + desplazar) % len(alfabeto)
            texto_encriptado += alfabeto[nuevo_indice]
    print(f'Texto plano: {mensaje}')
    print(f'Text encriptado: {texto_encriptado}')