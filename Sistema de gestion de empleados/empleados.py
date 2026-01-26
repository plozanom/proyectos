class Empleado:
    def __init__(self, nombre, id, salario):
        self.nombre = nombre
        self.id = id
        self.salario = salario

    def informacion(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nSalario: {self.salario}"


class Administrador(Empleado):
    def __init__(self, nombre, id, salario, departamento):
        super().__init__(nombre, id, salario)
        self.departamento = departamento

    def informacion(self):
        return f"{super().informacion()}\nDepartamento: {self.departamento}"


empleado = Administrador("Pepe", "01", 2000, "HR")
print(empleado.informacion())
