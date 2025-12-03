"""Reto: Generador de Tablas de Multiplicar Personalizado:
    - Pide al usuario un número y hasta qué número quiere la tabla de multiplicar.
    - Genera e imprime la tabla de multiplicar para ese número hasta el límite especificado.
    - Usa bucles.
Variación: Permite al usuario generar tablas para un rango de números (ej: tablas del 5 al 10)."""
from operacion import crear_tabla
import os

def clear_screen():
    """Limpia la pantalla de la terminal."""
    
    # Para sistemas Unix/Linux/macOS
    if os.name == 'posix':
        _ = os.system('clear')
    # Para sistemas Windows
    else:
        _ = os.system('cls')

while True:
    title = 'GENERADOR DE TABLAS DE MULTIPLICAR'
    ancho = 60

    clear_screen()

    print("=" * ancho)
    print(f"{title.center(ancho)}")
    print("=" * ancho)
    print("1. Generar una tabla de multiplicar\n2. Generar tablas de multiplicar en un rango")
    print("*" * ancho)
    print("0. Salir del menu")
    print("-" * ancho)

    eleccion = str(input("Por favor elija una opción: "))
    print("-" * ancho)

    clear_screen()

    if eleccion == '1':
        tabla = int(input("Ingrese el numero de la tabla de multiplicar: "))
        table_size = int(input("Hasta qué numero quiere su tabla de multiplicar? "))
        
        print()
        crear_tabla(tabla, table_size)

        input("\nPresione la tecla Enter para volver al menu...")
    elif eleccion == '2':
        inicio_rango = int(input("Ingrese desde que tabla quiere que inicie: "))
        final_rango = int(input("Ingrese en que tabla quiere que finalice: "))
        print("-" * ancho)
        table_size = int(input("Hasta qué numero quiere su tabla de multiplicar? "))
        print()
        
        for i in range(inicio_rango, final_rango + 1):
            crear_tabla(i, table_size)
        
        input("Presione la tecla Enter para volver al menu...")
    elif eleccion == '0':
        print("Ha salido de la aplicacion.")
        break
    else:
        print("Opcion incorrecta.")