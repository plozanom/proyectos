from simple_term_menu import TerminalMenu


def menu():
    opciones = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4", "Salir"]

    principal = TerminalMenu(opciones)
    _ = principal.show()


menu()
