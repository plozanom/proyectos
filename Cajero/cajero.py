import os

usuario = {'saldo': 100000}

while True:
    os.system('clear')
    print('\tMENU CAJERO\n')
    print('Selecciona una opcion del menu\n')
    print('\t1 - Ver saldo')
    print('\t2 - Sacar dinero')
    print('\t3 - Depositar saldo')
    print('\t0 - Salir')
    eleccion = int(input('Digite su seleccion: '))

    if eleccion == 1:
        print('Su saldo es de',usuario['saldo'])
        input('Pulsa cualquier tecla para continuar...')
    elif eleccion == 2:
        monto = int(input('Digite el monto a sacar: '))
        if monto <= usuario['saldo']:
            usuario['saldo'] = usuario['saldo'] - monto
            print('\nTransaccion exitosa!!\nUsted ha sacado '+str(monto)+', su saldo actual es de',usuario['saldo'])
            input('Pulsa cualquier tecla para continuar...')
        else:
            input('\nSu saldo es insuficiente\nPulsa cualquier tecla para continuar...')
    elif eleccion == 3:
        monto = int(input('Digite el monto a depositar: '))
        if monto >= 0:
            usuario['saldo'] = usuario['saldo'] + monto
            print('\nTransaccion exitosa!!\nUsted ha depositado '+str(monto)+', su saldo actual es de',usuario['saldo'])
            input('Pulsa cualquier tecla para continuar...')
        else:
            input('\nColoque un valor admisible\nPulsa cualquier tecla para continuar...')
    elif eleccion == 0:
        print('\nGracias por usar nuestros servicios!!!.')
        break
    else:
        input('\nSu seleccion no coressponde con ninguna opcion\nPulse cualquier tecla para continuar...')