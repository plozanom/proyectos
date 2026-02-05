from cpu import CPU
from dispositivo import Monitor, Mouse, Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, modelo, monitor, teclado, mouse, cpu):
        Computadora.contador_computadora += 1
        self.id = Computadora.contador_computadora
        self.modelo = modelo
        self.monitor = monitor
        self.teclado = teclado
        self.mouse = mouse
        self.cpu = cpu

    def __str__(self):
        return f"{5 * '*'} Computadora {self.id} Modelo {self.modelo} {5 * '*'}\n\n{5 * '*'} Monitor {5 * '*'}\n{self.monitor}\n\n{5 * '*'} Teclado {5 * '*'}\n{self.teclado}\n\n{5 * '*'} Mouse {5 * '*'}\n{self.mouse}\n\n{5 * '*'} CPU {5 * '*'}\n{self.cpu}"


# Priuebas
if __name__ == "__main__":
    monitor = Monitor("MSI", "Salida", "Display Port", 32)
    teclado = Teclado("Epomaker", "Entrada", "USB")
    mouse = Mouse("Razer", "Entrada", "USB")
    cpu = CPU("Asrock", "AMD", 32, "AMD")
    computadora = Computadora("Infinix", monitor, teclado, mouse, cpu)
    print(computadora)
