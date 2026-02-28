from inicializadores.inicializador import inicializar_db


# Advertencia: Si usas basedpyright, el idiota no reconocerá el decorador, por lo que marcará las funciones en rojo porque no 've' la conexión con sqlite
def main():
    inicializar_db()


if __name__ == "__main__":
    main()
