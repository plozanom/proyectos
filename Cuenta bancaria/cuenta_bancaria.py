class Cuenta_bancaria:
    def __init__(self, monto) -> None:
        self.depositado = 0
        self.monto = monto

    def depositos(self):
        self.depositado += self.monto
        return "Deposito exitoso"

    def retiros(self):
        if self.depositado < self.monto:
            return "No tiene suficiente dinero en la cuenta para la transacción"

        self.depositado -= self.monto
        return "Retiro exitoso"

    def balance(self):
        pass
