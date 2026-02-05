class Pedido:
    contador_pedido = 0

    def __init__(self, computadoras: list):
        Pedido.contador_pedido += 1
        self.id = Pedido.contador_pedido
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        info_pedido = ""

        for computadora in self.computadoras:
            info_pedido = f"\n{computadora.__str__()}"

        return f"Pedido nro: {self.id}\nDetalles: {info_pedido}"
