from utils import *
from distancia import *

def main():

    while True:
        menu = ["Kilometros a m", "Hectometros a m", "Decametros a m", "decimetros a m", "centimetros a m", "milimetros a m", "micrometros a m", "nanometros a m",
                "pulgadas a pies", "pies a yardas", "yardas a millas", "millas nauticas a pies", "pulgadas a centimetros", "centimetros a pulgadas", "pulgadas a metros",
                "metros a pulgadas", "pies a metros", "metros a pies", "millas a Kilometros", "Kilometros a millas", "millas nauticas a Kilometros", "Kilometros a millas nauticas"]
        display_menu("CONVERSOR DE DISTANCIAS", menu)
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            clear_screen()
            kilometros = float(input("Ingrese los kilometros a convertir: "))
            metros = Km_a_m(kilometros)
            print(f"{kilometros} kilometros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            clear_screen()
            hectometros = float(input("Ingrese los hectometros a convertir: "))
            metros = Hm_a_m(hectometros)
            print(f"{hectometros} hectometros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            clear_screen()
            decametros = float(input("Ingrese los decametros a convertir: "))
            metros = Dm_a_m(decametros)
            print(f"{decametros} decametros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            clear_screen()
            decimetros = float(input("Ingrese los decimetros a convertir: "))
            metros = dm_a_m(decimetros)
            print(f"{decimetros} decimetros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "5":
            clear_screen()
            centimetros = float(input("Ingrese los centimetros a convertir: "))
            metros = cm_a_m(centimetros)
            print(f"{centimetros} centimetros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "6":
            clear_screen()
            milimetros = float(input("Ingrese los milimetros a convertir: "))
            metros = mm_a_m(milimetros)
            print(f"{milimetros} milimetros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "7":
            clear_screen()
            micrometros = float(input("Ingrese los micrometros a convertir: "))
            metros = um_a_m(micrometros)
            print(f"{micrometros} micrometros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "8":
            clear_screen()
            nanometros = float(input("Ingrese los nanometros a convertir: "))
            metros = nm_a_m(nanometros)
            print(f"{nanometros} nanometros equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "9":
            clear_screen()
            pulgadas = float(input("Ingrese las pulgadas a convertir: "))
            pies = in_a_ft(pulgadas)
            print(f"{pulgadas} pulgadas equivalen a {pies} pies")
            input("\nPresiona Enter para continuar...")
        elif opcion == "10":
            clear_screen()
            pies = float(input("Ingrese los pies a convertir: "))
            yardas = ft_a_yd(pies)
            print(f"{pies} pies equivalen a {yardas} yardas")
            input("\nPresiona Enter para continuar...")
        elif opcion == "11":
            clear_screen()
            yardas = float(input("Ingrese las yardas a convertir: "))
            millas = yd_a_mi(yardas)
            print(f"{yardas} yardas equivalen a {millas} millas")
            input("\nPresiona Enter para continuar...")
        elif opcion == "12":
            clear_screen()
            millas_n = float(input("Ingrese las millas nauticas a convertir: "))
            pies = nmi_a_ft(millas_n)
            print(f"{millas_n} millas nauticas equivalen a {pies} pies")
            input("\nPresiona Enter para continuar...")
        elif opcion == "13":
            clear_screen()
            pulgadas = float(input("Ingrese las pulgadas a convertir: "))
            centimetros = in_a_cm(pulgadas)
            print(f"{pulgadas} pulgadas equivalen a {centimetros} centimetros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "14":
            clear_screen()
            centimetros = float(input("Ingrese los centimetros a convertir: "))
            pulgadas = cm_a_in(centimetros)
            print(f"{centimetros} centimetros equivalen a {pulgadas} pulgadas")
            input("\nPresiona Enter para continuar...")
        elif opcion == "15":
            clear_screen()
            pulgadas = float(input("Ingrese las pulgadas a convertir: "))
            metros = in_a_m(pulgadas)
            print(f"{pulgadas} pulgadas equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "16":
            clear_screen()
            metros = float(input("Ingrese los metros a convertir: "))
            pulgadas = m_a_in(metros)
            print(f"{metros} metros equivalen a {pulgadas} pulgadas")
            input("\nPresiona Enter para continuar...")
        elif opcion == "17":
            clear_screen()
            pies = float(input("Ingrese los pies a convertir: "))
            metros = ft_a_m(pies)
            print(f"{pies} pies equivalen a {metros} metros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "18":
            clear_screen()
            metros = float(input("Ingrese los metros a convertir: "))
            pies = m_a_ft(metros)
            print(f"{metros} metros equivalen a {pies} pies")
            input("\nPresiona Enter para continuar...")
        elif opcion == "19":
            clear_screen()
            millas = float(input("Ingrese las millas a convertir: "))
            kilometros = mi_a_km(millas)
            print(f"{millas} millas equivalen a {kilometros} kilometros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "20":
            clear_screen()
            kilometros = float(input("Ingrese los kilometros a convertir: "))
            millas = km_a_mi(kilometros)
            print(f"{kilometros} kilometros equivalen a {millas} millas")
            input("\nPresiona Enter para continuar...")
        elif opcion == "21":
            clear_screen()
            millas_n = float(input("Ingrese las millas nauticas a convertir: "))
            kilometros = nmi_a_km(millas_n)
            print(f"{millas_n} millas nauticas equivalen a {kilometros} kilometros")
            input("\nPresiona Enter para continuar...")
        elif opcion == "22":
            clear_screen()
            kilometros = float(input("Ingrese los kilometros a convertir: "))
            millas_n = nmi_a_km(kilometros)
            print(f"{kilometros} kilometros equivalen a {millas_n} millas nauticas")
            input("\nPresiona Enter para continuar...")
        elif opcion == "0":
            clear_screen()
            break
        else:
            clear_screen()
            print(f"{opcion} no es una opción dentro de la lista.\nPor favor ingrese una opción valida")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()