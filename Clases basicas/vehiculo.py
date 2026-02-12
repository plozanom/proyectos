class Vehiculo:
    numero_total_vehiculos = 0

    def __init__(self) -> None:
        Vehiculo.numero_total_vehiculos += 1

    def conducir(self):
        print("Se operan los mandos para controlar el movimiento y dirección")


class Coche(Vehiculo):
    def __init__(self) -> None:
        super().__init__()

    def conducir(self):
        print(
            "Se coordinan el volante y pedales para controlar el movimiento y dirección"
        )


class Moto(Vehiculo):
    def __init__(self) -> None:
        super().__init__()

    def conducir(self):
        print("Se equilibra el cuerpo mientras se controla el manubrio")
