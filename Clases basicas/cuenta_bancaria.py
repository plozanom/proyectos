class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
            return "Se actualizó el saldo de manera exitosa"
        else:
            return "No se puede hacer ese tipo de operación"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo = self.__saldo + cantidad
            return f"Se depositaron ${cantidad} de manera exitosa"
        else:
            return "No se puede hacer ese tipo de operación"
