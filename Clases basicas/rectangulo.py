class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # Aquí @property "transforma" el metodo area() en una variable area, pero esta variable es de solo lectura
    # En vez de llamar al metodo usando objeto.area(), se puede solo usar objeto.area
    @property
    def area(self):
        return self.ancho * self.alto
