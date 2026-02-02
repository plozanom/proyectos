class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"
