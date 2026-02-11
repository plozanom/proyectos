class Estudiante:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.cursos = []

    def inscribir_curso(self, nombre_curso: str):
        self.cursos.append(nombre_curso)

    def mostrar_cursos(self):
        for curso in self.cursos:
            print(curso)


if __name__ == "__main__":
    estudiante1 = Estudiante("Pepe", 15)
    estudiante1.inscribir_curso("Matemáticas")
    estudiante1.inscribir_curso("Biología")
    estudiante1.inscribir_curso("Ciencias Sociales")
    estudiante1.inscribir_curso("Filosofía")
    estudiante1.mostrar_cursos()
