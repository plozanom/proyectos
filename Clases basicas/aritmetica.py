class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

    def multiplicacion(self):
        return self.operando1 * self.operando2

    def division(self):
        return self.operando1 / self.operando2

    def div_exacta(self):
        return self.operando1 // self.operando2

    def modulo(self):
        return self.operando1 % self.operando2
