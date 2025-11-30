from temperatura import *
from utils import *

def menu():
    
    while True:
        menu_options = ["Celsius a Fahrenheit", "Fahrenheir a Celsius", "Celsius a Kelvin", "Kelvin a Celsius", "Fahrenheit a Kelvin", "Kelvin a Fahrenheit"]

        display_menu("CONVERSOR DE TEMPERATURA", menu_options)
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            clear_screen()

            celsius = float(input("Ingrese los grados Celsius a convertir: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}ºC equivalen a {fahrenheit}ºF")
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "2":
            clear_screen()

            fahrenheit = float(input("Ingrese los grados Fahrenheit a convertir: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}ºF equivalen a {celsius}ºC")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            clear_screen()

            celsius = float(input("Ingrese los grados Celsius a convertir: "))
            kelvin = celsius_a_kelvin(celsius)
            print(f"{celsius}ºC equivalen a {kelvin}K")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            clear_screen()

            kelvin = float(input("Ingrese los grados Kelvin a convertir: "))
            celsius = kelvin_a_celsius(kelvin)
            print(f"{kelvin}K equivalen a {celsius}ºC")
            input("\nPresiona Enter para continuar...")

        elif opcion == "5":
            clear_screen()

            fahrenheit = float(input("Ingrese los grados Fahrenheit a convertir: "))
            kelvin = fahrenheit_a_kelvin(fahrenheit)
            print(f"{fahrenheit}ºF equivalen a {kelvin}K")
            input("\nPresiona Enter para continuar...")

        elif opcion == "6":
            clear_screen()

            kelvin = float(input("Ingrese los grados Kelvin a convertir: "))
            fahrenheit = kelvin_a_fahrenheit(kelvin)
            print(f"{kelvin}K equivalen a {fahrenheit}ºF")
            input("\nPresiona Enter para continuar...")

        elif opcion == "0":
            clear_screen()
            print("Usted ha elegido cerrar el programa\nQue tenga un buen día")
            break
        else:
            clear_screen()
            print(f'{opcion} no es una opción dentro de la lista.\nPor favor ingrese una opción valida')
            input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    menu()