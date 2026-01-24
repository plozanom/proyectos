class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.esta_prestado = False

    def mostrar_info(self):
        if self.esta_prestado:
            estado = "Prestado"
        else:
            estado = "Disponible"

        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nEstado: {estado}"


class Usuario:
    pass


class Prestamo:
    pass
