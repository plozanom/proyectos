from tqdm import tqdm


def barra_progreso():
    bucle = tqdm(total=10000, position=0, leave=False)

    for i in range(10000):
        bucle.set_description("Cargando...".format(i))
        bucle.update(1)
    bucle.close()


barra_progreso()
