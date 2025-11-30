from random import randint

aleatorio = randint(1,100)

adivinar = int(input('\nCrees que puedes adivinar el numero (entre 1 y 99) en menos de 10 intentos?\nIntenta con tu primer numero: '))

intentos = 9

while aleatorio != adivinar:
    if aleatorio > adivinar:
        adivinar = int(input(f'\nTu numero es menor que el numero a adivinar\nVamos, te quedan {intentos} intentos!.\nPrueba con otro numero: '))
    else:
        adivinar = int(input(f'\nTu numero es mayor que el numero a adivinar\nVamos, te quedan {intentos} intentos!.\nPrueba con otro numero: '))
    
    intentos -= 1

    if intentos == 0:
        print('\nHas perdido. Mejor suerte para la otra')
        break

if aleatorio == adivinar:
    print(f'\nFelicitaciones! Has adivinado el numero correctamente y te quedaron {intentos} intentos!')