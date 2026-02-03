class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property  # En este caso, el decorador @property funciona como get o getter, pero no es su unica función
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
            return "Se actualizó el saldo de manera exitosa"
        else:
            return "No se puede hacer ese tipo de operación"

    # Se pueden pasar parametros a los metodos, ya que solo afecta al metodo cuando se utiliza, no sería buena idea ponerlo en el constructor
    # Es más, en este caso, ya que es un deposito, no se puede colocar tal cosa en el constructor al instanciar
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo = self.__saldo + cantidad
            return f"Se depositaron ${cantidad} de manera exitosa"
        else:
            return "No se puede hacer ese tipo de operación"
