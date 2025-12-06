import os

def clear_screen():
    """Limpia la pantalla de la terminal."""
    
    # Para sistemas Unix/Linux/macOS
    if os.name == 'posix':
        _ = os.system('clear')
    # Para sistemas Windows
    else:
        _ = os.system('cls')

def display_menu(title, options):
    """
    Muestra un menú en la terminal y devuelve la opción seleccionada por el usuario.
    """
    clear_screen()
    print("=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    print("-" * 40)
    print("0. Salir")
    print("=" * 40)