from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self):
        self.id_persona = 0
        self.nombre = ""
        self.direccion = ""
        self.email = ""
        self.telefono = ""

    @abstractmethod
    def detalles_basicos(self):
        pass


class Maestro(Persona):
    def __init__(self, salario, especialidad, tiempo_inicio):
        self.salario = salario
        self.especialidad = especialidad
        self.__tiempo_inicio = tiempo_inicio

    def detalles_basicos(self):
        print(f"El profesor {self.nombre}, tiene un salario de ${self.salario}")

    def puede_retirarse(self):
        return self.__tiempo_de_servicio() >= 30

    def __tiempo_de_servicio(self):
        return 2026 - self.__tiempo_inicio


class Estudiante(Persona):
    def __init__(self, nombre_acudiente="", contacto_acudiente="", estado=""):
        self.nombre_acudiente = nombre_acudiente
        self.contacto_acudiente = contacto_acudiente
        self.__estado = estado

    def detalles_basicos(self):
        print(f"El alumno {self.nombre} tiene de tutor a {self.nombre_acudiente}")

    def detalles_del_tutor(self):
        print(
            f"Nombre del tutor: {self.nombre_acudiente}\nContacto: {self.contacto_acudiente}"
        )


class Curso:
    def __init__(self, id_curso, nombre, requisitos, creditos_minimos):
        self.id_curso = id_curso
        self.nombre = nombre
        self.requisitos = requisitos
        self.__creditos_minimos = creditos_minimos

    def tiene_creditos_minimos(self, calificacion):
        return calificacion > self.__creditos_minimos


class Calificaciones:
    def __init__(self, id_calificacion, calificacion, estudiante, curso):
        self.id_calificacion = id_calificacion
        self.calificacion = calificacion
        self.estudiante = estudiante
        self.curso = curso

    def pasa_curso(self):
        if self.curso.tiene_creditos_minimos(self.calificacion):
            print(
                f"El estudiante {self.estudiante.nombre} pasó el curso de {self.curso.nombre}"
            )
        else:
            print(
                f"El estudiante {self.estudiante.nombre} reprobó el curso de {self.curso.nombre}"
            )
