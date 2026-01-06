import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def mostrar_logo():
    logo = r"""
    ___  ___ _____  _   _  _   _ 
    |  \/  ||  ___|| \ | || | | |
    | .  . || |__  |  \| || | | |
    | |\/| ||  __| | . ` || | | |
    | |  | || |___ | |\  || |_| |
    \_|  |_/\____/ \_| \_/ \___/ 
                                 
      Bienvenido al Sistema v1.0
    =============================
    """
    print(logo)

def opciones():
    print("  [1] Buscar usuario")
    print("  [2] Configuración")
    print("  [3] Ayuda")
    print("  [0] Salir")
    print("\n" + "="*29)

def menu(input):
    limpiar_pantalla()
    mostrar_logo()

    opciones()

    print(f"Selecione una opción: {input}")