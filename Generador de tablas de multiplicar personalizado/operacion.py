def crear_tabla(num, size):

    title = f'TABLA DE MULTIPLICAR DEL {num}'
    ancho = 60

    print("=" * ancho)
    print(f"{title.center(ancho)}")
    print("=" * ancho)

    for _ in range(size):
        print(f'{num} x {_ + 1} = {num * (_ + 1)}')
    
    print()