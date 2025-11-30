from area import *
from utils import *

def main_menu():

    while True:
        menu_options = ["Area del circulo", "Area del triangulo", "Area del cuadrado", "Area del rectangulo"]

        display_menu("CALCULADORA DE AREA", menu_options)
        opcion = str(input("Elige una opcion: "))

        if opcion == "1":
            clear_screen()

            radio = float(input("Ingrese el radio de la circunferencia: "))
            circulo = area_circulo(radio)
            print(f"El area del circulo con radio {radio} es {circulo}")
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "2":
            clear_screen()

            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            triangulo = area_triangulo(base, altura)
            print(f"El area del triangulo con base {base} y altura {altura} es {triangulo}")
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "3":
            clear_screen()

            lado = float(input("Ingrese un lado del cuadrado: "))            
            cuadrado = area_cuadrado(lado)
            print(f"El area del cuadrado de lado {lado} es {cuadrado}")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            clear_screen()

            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rectangulo = area_rectangulo(base, altura)
            print(f"El area del rectangulo con base {base} y altura {altura} es {rectangulo}")
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "5":
            clear_screen()

            base1 = float(input("Ingrese la base mayor del trapecio: "))
            base2 = float(input("Ingrese la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            trapecio = area_trapecio(base1, base2, altura)
            print(f"El area del trapecio con base mayor {base1}, base menor {base2} y altura {altura} es {trapecio}")
            input("\nPresiona Enter para continuar...")

        elif opcion == "6":
            clear_screen()

            mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            menor = float(input("Ingrese la diagonal menor del rombo: "))
            rombo = area_rombo(mayor, menor)
            print(f"El area del rombo con diagonal mayor {mayor} y diagonal menor {menor} es {rombo}")
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
    main_menu()