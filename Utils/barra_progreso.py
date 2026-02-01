from time import sleep

from tqdm import tqdm


def barra_progreso():
    bucle = tqdm(total=100, position=0, leave=False)

    for i in range(100):
        bucle.set_description(f"Cargando... {i}")
        sleep(0.1)
        _ = bucle.update(1)
    bucle.close()


barra_progreso()
