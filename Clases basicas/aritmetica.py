class Aritmetica:
    def __init__(self, operando1, operando2):
        self.__operando1 = operando1
        self.__operando2 = operando2

    @property
    def operando1(self):
        return self.__operando1

    @property
    def operando2(self):
        return self.__operando2

    @operando1.setter
    def operando1(self, operando1):
        self.__operando1 = operando1

    @operando2.setter
    def operando2(self, operando2):
        self.__operando2 = operando2

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

    def multiplicacion(self):
        return self.operando1 * self.operando2

    def division(self):
        try:
            return self.operando1 / self.operando2
        except ZeroDivisionError:
            return "No se puede dividir entre cero"

    def div_exacta(self):
        try:
            return self.operando1 // self.operando2
        except ZeroDivisionError:
            return "No se puede dividir entre cero"

    def modulo(self):
        try:
            return self.operando1 % self.operando2
        except ZeroDivisionError:
            return "No se puede dividir entre cero"
