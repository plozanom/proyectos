# Cifrado Cesar sencillo

def cesar(mensaje, desplazar):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in mensaje.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + desplazar) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', mensaje)
    print('encrypted text:', encrypted_text)