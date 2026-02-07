class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.esta_prestado = False

    def mostrar_info(self):
        if self.esta_prestado:
            estado = "Prestado"
        else:
            estado = "Disponible"

        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nGenero: {self.genero}\nEstado: {estado}"


class Usuario:
    def __init__(self, nombre, edad):
        self.tarjeta = False
        self.nombre = nombre
        self.edad = edad

    def info_usuario(self):
        if self.tarjeta:
            membresia = "Tiene credenciales"
        else:
            membresia = "Debe diligenciar la membresía"

        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nMembresía: {membresia}"


class Prestamo(Libro, Usuario):
    def __init__(self, titulo, autor, genero, nombre, edad, libros_prestados):
        Libro.__init__(self, titulo, autor, genero)
        Usuario.__init__(self, nombre, edad)
        self.libros_prestados = libros_prestados

    def maximo_prestamo_libros(self):
        if self.edad >= 18:
            return 5
        else:
            return 2

    def puede_prestar_libros(self):
        if self.maximo_prestamo_libros() > self.libros_prestados:
            return "Puede prestar libros"
        else:
            return "No puede prestar más libros"
