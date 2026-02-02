class Lampara:
    def __init__(self):
        self.encendida = False

    def encender(self):
        if not self.encendida:
            self.encendida = True

        return self.encendida

    def apagar(self):
        if self.encendida:
            self.encendida = False

        return self.encendida
