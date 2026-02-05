class Dispositivo:
    def __init__(self, marca, tipo, conexion):
        self.marca = marca
        self.tipo = tipo  # Entrada/Salida
        self.conexion = conexion  # USB/Bluetooth/HDMI etc.


class Mouse(Dispositivo):
    contador_mouse = 0

    def __init__(self, marca, tipo, conexion):
        super().__init__(marca, tipo, conexion)
        Mouse.contador_mouse += 1
        self.id = Mouse.contador_mouse

    def __str__(self):
        return f"ID: {self.id}\nMarca: {self.marca}\nTipo de dispositivo: {self.tipo}\nTipo de conexión: {self.conexion}"


class Teclado(Dispositivo):
    contador_teclado = 0

    def __init__(self, marca, tipo, conexion):
        super().__init__(marca, tipo, conexion)
        Teclado.contador_teclado += 1
        self.id = Teclado.contador_teclado

    def __str__(self):
        return f"ID: {self.id}\nMarca: {self.marca}\nTipo de dispositivo: {self.tipo}\nTipo de conexión: {self.conexion}"


class Monitor(Dispositivo):
    contador_monitor = 0

    def __init__(self, marca, tipo, conexion, pulgadas):
        super().__init__(marca, tipo, conexion)
        Monitor.contador_monitor += 1
        self.id = Monitor.contador_monitor
        self.pulgadas = pulgadas

    def __str__(self):
        return f"ID: {self.id}\nMarca: {self.marca}\nPulgadas: {self.pulgadas}\nTipo de dispositivo: {self.tipo}\nTipo de conexión: {self.conexion}"
